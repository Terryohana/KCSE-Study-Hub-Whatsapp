import os
import sys
import json
import argparse
import datetime
import requests

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

TIME_SLOTS = [
    ("07:00 AM", 7, 0, 1),
    ("07:30 AM", 7, 30, 2),
    ("08:00 AM", 8, 0, 3),
    ("08:30 AM", 8, 30, 4),
    ("09:00 AM", 9, 0, 5),
    ("09:30 AM", 9, 30, 6),
    ("10:00 AM", 10, 0, 7),
    ("10:30 AM", 10, 30, 8),
    ("11:00 AM", 11, 0, 9),
    ("11:30 AM", 11, 30, 10),
    ("12:00 PM", 12, 0, 11),
]

DAY_BANKS = {
    0: "monday_math.json",
    1: "tuesday_languages.json",
    2: "wednesday_physical_sciences.json",
    3: "thursday_biological_sciences.json",
    4: "friday_humanities.json",
    5: "saturday_technicals.json",
    6: "sunday_grand_review.json"
}

def get_eat_now():
    """Return current datetime in East Africa Time (UTC+3)"""
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    eat_tz = datetime.timezone(datetime.timedelta(hours=3))
    return utc_now.astimezone(eat_tz)

def determine_slot(eat_now, manual_slot=None):
    if manual_slot is not None and 1 <= manual_slot <= 11:
        for label, h, m, slot_num in TIME_SLOTS:
            if slot_num == manual_slot:
                return label, slot_num
        return TIME_SLOTS[manual_slot - 1][0], manual_slot

    current_minutes = eat_now.hour * 60 + eat_now.minute
    best_slot = None
    min_diff = 99999

    for label, h, m, slot_num in TIME_SLOTS:
        target_minutes = h * 60 + m
        diff = abs(current_minutes - target_minutes)
        if diff < min_diff:
            min_diff = diff
            best_slot = (label, slot_num)

    return best_slot

def main():
    parser = argparse.ArgumentParser(description="Post scheduled KCSE revision questions to WhatsApp")
    parser.add_argument("--slot", type=int, default=None, help="Force specific slot (1-11)")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending to WhatsApp")
    args = parser.parse_args()

    api_url = os.environ.get('WHATSAPP_API_URL', 'https://7107.api.greenapi.com').rstrip('/')
    instance_id = os.environ.get('WHATSAPP_INSTANCE_ID', '710722732605')
    token = os.environ.get('WHATSAPP_API_TOKEN', '14f3ba786ec84b14b4c631a3ffd2c8e1fb32f9782bda45198e')
    group_id = os.environ.get('WHATSAPP_GROUP_ID', '120363414303629222@g.us')

    eat_now = get_eat_now()
    weekday = eat_now.weekday() # 0 = Monday, 6 = Sunday
    week_number = eat_now.isocalendar()[1] # 1 to 53

    slot_label, slot_number = determine_slot(eat_now, args.slot)

    # Load appropriate bank
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bank_filename = DAY_BANKS.get(weekday, "monday_math.json")
    bank_path = os.path.join(script_dir, 'questions_bank', bank_filename)

    if not os.path.exists(bank_path):
        print(f"Error: Question bank {bank_path} not found. Running generator...")
        import generate_questions_bank
        generate_questions_bank.build_full_banks()

    with open(bank_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Find the question for this (week, slot)
    selected = None
    for q in questions:
        if q.get("week") == week_number and q.get("slot") == slot_number:
            selected = q
            break

    if not selected:
        # Fallback to modulo indexing
        idx = ((week_number - 1) * 11 + (slot_number - 1)) % len(questions)
        selected = questions[idx]

    date_str = eat_now.strftime("%A, %d %B %Y")

    # Difficulty stars based on slot number
    if slot_number <= 3:
        difficulty = "⭐⭐☆☆☆ (Foundational Drill)"
        est_time = "10 Mins"
    elif slot_number <= 7:
        difficulty = "⭐⭐⭐☆☆ (Standard KNEC Level)"
        est_time = "15 Mins"
    elif slot_number <= 10:
        difficulty = "⭐⭐⭐⭐☆ (High-Yield Challenge)"
        est_time = "20 Mins"
    else:
        difficulty = "⭐⭐⭐⭐⭐ (Distinction A-Tier)"
        est_time = "25 Mins"

    message = (
        f"╔══════════════════════════╗\n"
        f"  🎓 *KCSE STUDY HUB REVISION* 🇰🇪\n"
        f"╚══════════════════════════╝\n"
        f"📅 *{date_str}* | ⏰ *{slot_label}*\n"
        f"🏷️ *Theme:* {selected['day_theme']}\n"
        f"📖 *Paper:* {selected['paper']}\n"
        f"⚡ *Difficulty:* {difficulty}\n"
        f"⏱️ *Target Time:* {est_time}\n\n"
        f"📍 *TOPIC:* {selected['topic']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"❓ *QUESTION (Slot {slot_number}/11):*\n"
        f"{selected['question']}\n\n"
        f"💡 *EXAMINER TIP / KEY METHOD:*\n"
        f"{selected['tip']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💬 *Challenge:* Attempt this question and share your answer below! ✍️\n\n"
        f"📲 *Check Complete Marking Scheme on KCSE Study Hub:*\n"
        f"https://play.google.com/store/apps/details?id=com.revisekenya.kcsehub"
    )

    print("=" * 60)
    print(f"Target: {group_id}")
    print(f"Time (EAT): {eat_now.strftime('%Y-%m-%d %H:%M:%S')} | Week {week_number} | Slot {slot_number} ({slot_label})")
    print(f"File: {bank_filename}")
    print("=" * 60)
    print(message)
    print("=" * 60)

    if args.dry_run:
        print("Dry run completed. Message not sent.")
        return

    send_url = f"{api_url}/waInstance{instance_id}/sendMessage/{token}"
    payload = {
        "chatId": group_id,
        "message": message
    }

    try:
        response = requests.post(send_url, json=payload, timeout=25)
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        if response.status_code == 200:
            print("Message sent successfully to WhatsApp group!")
        else:
            print(f"Warning: Unexpected status {response.status_code}")
    except Exception as e:
        print(f"Error sending message: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
