#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔥 WINGO 1M - 19 UNIQUE HACKS MEGA FUSION BOT
🎯 19 Different Hack Algorithms
🗳️ Majority Vote → Prediction
📊 Hourly Report
📡 MODE: 1 MIN WINGO
"""

import asyncio
import time
import requests
import os
import random
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

try:
    from telegram import Bot
except ImportError:
    print("❌ python-telegram-bot not installed!")
    exit(1)

# ==================== কনফিগ ====================
BOT_TOKEN = "8386058038:AAEwayH-C4AUr7L_tx6Ecz__xpIXnrekJw0"
CHAT_ID = "5012028880"
API_URL = "https://draw.ar-lottery01.com/WinGo/WinGo_1M/GetHistoryIssuePage.json"

# ==================== ওয়েব সার্ভার ====================
class DummyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"19 HACKS MEGA FUSION BOT is running!")
    def log_message(self, format, *args):
        pass

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), DummyServer)
    print(f"🌐 Web Server started on port {port}")
    server.serve_forever()

server_thread = threading.Thread(target=run_dummy_server, daemon=True)
server_thread.start()

# ==================== বট ====================
bot = Bot(token=BOT_TOKEN)

# ==================== ডেটা ====================
total_wins = 0
total_losses = 0
total_jackpots = 0
total_rounds = 0
current_streak = 0
best_win_streak = 0
worst_loss_streak = 0

hourly_wins = 0
hourly_losses = 0
hourly_rounds = 0
hourly_best_win_streak = 0
hourly_worst_loss_streak = 0
hourly_current_streak = 0
hourly_current_streak_type = "WIN"
hourly_jackpots = 0

last_predicted_period = None
last_predicted_signal = None
last_predicted_num = None
prediction_sent_for_period = {}
last_result_sent = False
last_hour_report_time = time.time()

# ============================================================
# 🎯 19 UNIQUE HACK ALGORITHMS
# ============================================================

# 1. Crack By Kohli Mods
def h_kohli(h):
    if len(h) < 3: return 'BIG'
    l2 = h[:2]
    if l2[0] == l2[1]: return 'SMALL' if l2[0] == 'BIG' else 'BIG'
    return l2[0]

# 2. HACK KA BOSS - Gold Break
def h_hackboss(h):
    if len(h) < 10: return 'BIG'
    big = h[:10].count('BIG')
    if big >= 8: return 'SMALL'
    if big <= 2: return 'BIG'
    return 'BIG' if big > 5 else 'SMALL'

# 3. SHIKAARI BOSS
def h_shikaari(h, last_num):
    if last_num is None: return 'BIG'
    if len(h) >= 2 and h[0] == h[1]:
        r = 11 - last_num
        return 'BIG' if r >= 5 else 'SMALL'
    r = last_num - 1
    if r < 0: r = 9
    return 'BIG' if r >= 5 else 'SMALL'

# 4. WINGO INFINITY AI
def h_infinity(h):
    if len(h) < 5: return 'BIG'
    big = h[:5].count('BIG')
    streak = 1
    for i in range(1, len(h)):
        if h[i] == h[0]: streak += 1
        else: break
    if streak >= 4: return 'SMALL' if h[0] == 'BIG' else 'BIG'
    return 'BIG' if big >= 3 else 'SMALL'

# 5. PRIYANSHU PVT MOD
def h_priyanshu(h):
    if len(h) < 4: return 'BIG'
    l4 = h[:4]
    streak = 1
    for i in range(1, 4):
        if l4[i] == l4[0]: streak += 1
        else: break
    if streak >= 4: return 'SMALL' if l4[0] == 'BIG' else 'BIG'
    if l4[0] != l4[1] and l4[1] != l4[2]: return 'SMALL' if l4[0] == 'BIG' else 'BIG'
    if l4[0] == l4[1] and l4[2] == l4[3]: return 'SMALL' if l4[0] == 'BIG' else 'BIG'
    return 'BIG' if l4.count('BIG') >= 2 else 'SMALL'

# 6. SANJU BHAI AI
def h_sanju(h):
    if len(h) < 10: return 'BIG'
    big = h[:10].count('BIG')
    if big >= 8: return 'SMALL'
    if big <= 2: return 'BIG'
    return 'BIG' if big > 5 else 'SMALL'

# 7. MADMAX X PRO V6
def h_madmax(h):
    if len(h) < 5: return 'BIG'
    big = h[:5].count('BIG')
    streak = 1
    for i in range(1, len(h)):
        if h[i] == h[0]: streak += 1
        else: break
    if streak >= 3: return 'SMALL' if h[0] == 'BIG' else 'BIG'
    return 'BIG' if big >= 3 else 'SMALL'

# 8. CYBER PRO MAX
def h_cyber(h):
    if len(h) < 4: return 'BIG'
    big = h[:4].count('BIG')
    if big >= 3: return 'SMALL'
    if big <= 1: return 'BIG'
    return h[0]

# 9. ANSH BHAI AI
def h_ansh(h):
    if len(h) < 5: return 'BIG'
    return 'BIG' if h[:5].count('BIG') >= 3 else 'SMALL'

# 10. ANSH 2 LEVEL AI v6
def h_ansh2(h):
    if len(h) < 4: return 'BIG'
    big = h[:4].count('BIG')
    if big >= 3: return 'SMALL'
    if big <= 1: return 'BIG'
    return h[0]

# 11. ANSH PRO BEAST
def h_beast(h):
    if len(h) < 6: return 'BIG'
    score = 0
    for i, x in enumerate(h[:6]):
        score += (1 if x == 'BIG' else -1) * (6 - i)
    streak = 1
    for i in range(1, len(h)):
        if h[i] == h[0]: streak += 1
        else: break
    if streak >= 4: score = -score
    return 'BIG' if score >= 0 else 'SMALL'

# 12. PANDA PREDICTOR
def h_panda(h):
    if len(h) < 5: return 'BIG'
    big = h[:5].count('BIG')
    streak = 1
    for i in range(1, len(h)):
        if h[i] == h[0]: streak += 1
        else: break
    if streak >= 4: return 'SMALL' if h[0] == 'BIG' else 'BIG'
    return 'BIG' if big >= 3 else 'SMALL'

# 13. FLEXI V8
def h_flexi(h):
    if len(h) < 8: return 'BIG'
    big = h[:8].count('BIG')
    if big >= 6: return 'SMALL'
    if big <= 2: return 'BIG'
    return 'BIG' if big > 4 else 'SMALL'

# 14. REXAA ULTRA VIP
def h_rexaa(h):
    if len(h) < 5: return 'BIG'
    big = h[:5].count('BIG')
    streak = 1
    for i in range(1, len(h)):
        if h[i] == h[0]: streak += 1
        else: break
    if streak >= 4: return 'SMALL' if h[0] == 'BIG' else 'BIG'
    return 'BIG' if big >= 3 else 'SMALL'

# 15. YADAV NOVIX V1
def h_yadav(h):
    if len(h) < 6: return 'BIG'
    big = h[:6].count('BIG')
    streak = 1
    for i in range(1, len(h)):
        if h[i] == h[0]: streak += 1
        else: break
    if streak >= 3: return 'SMALL' if h[0] == 'BIG' else 'BIG'
    return 'BIG' if big >= 3 else 'SMALL'

# 16. FUN BY REAL
def h_funreal(h):
    if len(h) < 4: return 'BIG'
    big = h[:4].count('BIG')
    if big >= 3: return 'SMALL'
    if big <= 1: return 'BIG'
    return h[0]

# 17. FreeWorking
def h_freeworking(h):
    if len(h) < 10: return 'BIG'
    big = h[:10].count('BIG')
    if big >= 8: return 'SMALL'
    if big <= 2: return 'BIG'
    return 'BIG' if big > 5 else 'SMALL'

# 18. BABY
def h_baby(h):
    if len(h) < 10: return 'BIG'
    big = h[:10].count('BIG')
    if big >= 8: return 'SMALL'
    if big <= 2: return 'BIG'
    return 'BIG' if big > 5 else 'SMALL'

# 19. RAMU BOSS V2
def h_ramu(h):
    if len(h) < 4: return 'BIG'
    big = h[:4].count('BIG')
    return 'BIG' if big >= 2 else 'SMALL'

# All 19 Hacks
HACKS = [
    ("Kohli Mods", lambda h, n: h_kohli(h)),
    ("Hack Ka Boss", lambda h, n: h_hackboss(h)),
    ("Shikaari Boss", lambda h, n: h_shikaari(h, n)),
    ("Infinity AI", lambda h, n: h_infinity(h)),
    ("Priyanshu", lambda h, n: h_priyanshu(h)),
    ("Sanju Bhai", lambda h, n: h_sanju(h)),
    ("Madmax X", lambda h, n: h_madmax(h)),
    ("Cyber Pro", lambda h, n: h_cyber(h)),
    ("Ansh Bhai", lambda h, n: h_ansh(h)),
    ("Ansh 2Level", lambda h, n: h_ansh2(h)),
    ("Ansh Beast", lambda h, n: h_beast(h)),
    ("Panda Predictor", lambda h, n: h_panda(h)),
    ("Flexi V8", lambda h, n: h_flexi(h)),
    ("Rexaa Ultra", lambda h, n: h_rexaa(h)),
    ("Yadav Novix", lambda h, n: h_yadav(h)),
    ("Fun By Real", lambda h, n: h_funreal(h)),
    ("FreeWorking", lambda h, n: h_freeworking(h)),
    ("Baby Pattern", lambda h, n: h_baby(h)),
    ("RAMU Boss V2", lambda h, n: h_ramu(h))
]

# ============================================================
# 🗳️ MAJORITY VOTE ENGINE
# ============================================================
def mega_fusion_engine(history_sides, last_num):
    predictions = []
    for name, fn in HACKS:
        try:
            p = fn(history_sides, last_num)
            predictions.append(p)
        except Exception as e:
            predictions.append('BIG')
    
    big_votes = predictions.count('BIG')
    small_votes = predictions.count('SMALL')
    
    if big_votes > small_votes:
        final = 'BIG'
    elif small_votes > big_votes:
        final = 'SMALL'
    else:
        final = predictions[0]
    
    confidence = int((max(big_votes, small_votes) / len(predictions)) * 100)
    
    if final == 'BIG':
        num = random.randint(5, 9)
    else:
        num = random.randint(0, 4)
    
    return {
        'prediction': final,
        'number': num,
        'confidence': confidence,
        'big_votes': big_votes,
        'small_votes': small_votes,
        'total_votes': len(predictions),
        'predictions': predictions
    }

# ==================== API ====================
def fetch_api_data():
    try:
        url = API_URL + "?t=" + str(int(time.time() * 1000))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        }
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            return data.get("data", {}).get("list", [])
    except Exception as e:
        print(f"API Error: {e}")
    return []

# ==================== Telegram সেন্ড ====================
async def send_message(text):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")
        return True
    except Exception as e:
        print(f"Send error: {e}")
        return False

# ==================== হাওয়ারলি রিপোর্ট ====================
async def send_hourly_report():
    global hourly_wins, hourly_losses, hourly_rounds
    global hourly_best_win_streak, hourly_worst_loss_streak
    global hourly_current_streak, hourly_current_streak_type, hourly_jackpots
    global total_wins, total_losses, total_rounds, total_jackpots
    global best_win_streak, worst_loss_streak
    global last_hour_report_time

    if hourly_rounds == 0:
        return

    hourly_win_rate = (hourly_wins / hourly_rounds * 100) if hourly_rounds > 0 else 0
    total_win_rate = (total_wins / total_rounds * 100) if total_rounds > 0 else 0

    report_msg = (
        f"📊 *HOURLY REPORT - 19 HACKS (1M)*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🕐 *TIME:* {datetime.now().strftime('%I:%M %p')}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🔄 *HOURLY ROUNDS:* `{hourly_rounds}`\n"
        f"✅ *HOURLY WINS:* `{hourly_wins}`\n"
        f"❌ *HOURLY LOSSES:* `{hourly_losses}`\n"
        f"📈 *HOURLY WIN RATE:* `{hourly_win_rate:.1f}%`\n"
        f"🔥 *BEST WIN STREAK:* `{hourly_best_win_streak}x`\n"
        f"📉 *WORST LOSS STREAK:* `{hourly_worst_loss_streak}x`\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 *TOTAL ROUNDS:* `{total_rounds}`\n"
        f"✅ *TOTAL WINS:* `{total_wins}`\n"
        f"❌ *TOTAL LOSSES:* `{total_losses}`\n"
        f"💎 *JACKPOTS:* `{total_jackpots}`\n"
        f"📈 *TOTAL WIN RATE:* `{total_win_rate:.1f}%`\n"
        f"🔥 *BEST WIN STREAK:* `{best_win_streak}x`\n"
        f"📉 *WORST LOSS STREAK:* `{worst_loss_streak}x`\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ 19 HACKS MEGA FUSION"
    )

    await send_message(report_msg)

    hourly_wins = 0
    hourly_losses = 0
    hourly_rounds = 0
    hourly_best_win_streak = 0
    hourly_worst_loss_streak = 0
    hourly_current_streak = 0
    hourly_current_streak_type = "WIN"
    hourly_jackpots = 0
    last_hour_report_time = time.time()

# ==================== মেইন লুপ ====================
async def prediction_bot():
    global total_wins, total_losses, total_jackpots, total_rounds
    global hourly_wins, hourly_losses, hourly_rounds
    global hourly_best_win_streak, hourly_worst_loss_streak
    global hourly_current_streak, hourly_current_streak_type, hourly_jackpots
    global current_streak, best_win_streak, worst_loss_streak
    global last_predicted_period, last_predicted_signal, last_predicted_num
    global prediction_sent_for_period, last_result_sent
    global last_hour_report_time

    print("🔥 19 HACKS MEGA FUSION BOT STARTED...")
    print(f"📡 Total Hacks: {len(HACKS)}")
    print("🗳️ MAJORITY VOTE SYSTEM")
    print("📊 HOURLY REPORT: ENABLED")
    print("📡 MODE: 1 MIN WINGO")

    await send_message(
        "🔥 *WINGO 1M MEGA FUSION* 🔥\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"📡 *TOTAL HACKS:* `{len(HACKS)}`\n"
        "🗳️ *MAJORITY VOTE SYSTEM*\n"
        "📊 *HOURLY REPORT:* ENABLED\n"
        "📡 *MODE:* 1 MIN WINGO\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⏳ WAITING FOR FIRST SIGNAL..."
    )

    while True:
        try:
            current_sec = int(time.time()) % 60
            sleep_time = 60 - current_sec + 3
            await asyncio.sleep(sleep_time)

            raw_list = fetch_api_data()
            if not raw_list:
                print("⚠️ API ডেটা নেই")
                continue

            history_sides = []
            for h in raw_list[:20]:
                num = int(h['number'])
                history_sides.append("BIG" if num >= 5 else "SMALL")

            latest = raw_list[0]
            latest_issue = str(latest['issueNumber'])
            actual_num = int(latest['number'])
            actual_type = "BIG" if actual_num >= 5 else "SMALL"

            print(f"📡 PERIOD: {latest_issue}, NUMBER: {actual_num}")

            # ==================== RESULT CHECK ====================
            if last_predicted_period == latest_issue and last_predicted_signal is not None and not last_result_sent:
                is_win = (last_predicted_signal == actual_type)
                is_jackpot = (last_predicted_num == actual_num)

                if is_jackpot:
                    total_jackpots += 1
                    total_wins += 1
                    hourly_wins += 1
                    hourly_jackpots += 1
                    status = "💎 JACKPOT"
                    is_win = True
                elif is_win:
                    total_wins += 1
                    hourly_wins += 1
                    status = "✅ WIN"
                else:
                    total_losses += 1
                    hourly_losses += 1
                    status = "❌ LOSS"

                if is_win:
                    if current_streak >= 0:
                        current_streak += 1
                    else:
                        current_streak = 1
                else:
                    if current_streak <= 0:
                        current_streak -= 1
                    else:
                        current_streak = -1

                if current_streak > best_win_streak:
                    best_win_streak = current_streak
                if abs(current_streak) > worst_loss_streak and current_streak < 0:
                    worst_loss_streak = abs(current_streak)

                if is_win:
                    if hourly_current_streak_type == "WIN":
                        hourly_current_streak += 1
                    else:
                        hourly_current_streak = 1
                        hourly_current_streak_type = "WIN"
                    if hourly_current_streak > hourly_best_win_streak:
                        hourly_best_win_streak = hourly_current_streak
                else:
                    if hourly_current_streak_type == "LOSS":
                        hourly_current_streak += 1
                    else:
                        hourly_current_streak = 1
                        hourly_current_streak_type = "LOSS"
                    if hourly_current_streak > hourly_worst_loss_streak:
                        hourly_worst_loss_streak = hourly_current_streak

                total_rounds += 1
                hourly_rounds += 1

                total_win_rate = (total_wins / total_rounds * 100) if total_rounds > 0 else 0
                streak_emoji = "🔥" if current_streak > 0 else "📉" if current_streak < 0 else "⏸️"

                result_msg = (
                    f"🎯 *RESULT UPDATE*\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"🆔 PERIOD: `#{latest_issue[-5:]}`\n"
                    f"🎯 PREDICTED: `{last_predicted_signal}` → `{last_predicted_num}`\n"
                    f"🎰 ACTUAL: `{actual_num}` (`{actual_type}`)\n"
                    f"📌 RESULT: `{status}`\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"📊 WIN RATE: `{total_win_rate:.1f}%` ({total_wins}W/{total_losses}L)\n"
                    f"💎 JACKPOTS: `{total_jackpots}`\n"
                    f"{streak_emoji} STREAK: `{current_streak:+d}`\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚡ 19 HACKS MEGA FUSION"
                )

                await send_message(result_msg)
                print(f"📊 Result: {status}")

                last_result_sent = True
                last_predicted_period = None
                last_predicted_signal = None
                last_predicted_num = None

                if time.time() - last_hour_report_time >= 3600:
                    await send_hourly_report()

            # ==================== NEW PREDICTION ====================
            next_period = str(int(latest_issue) + 1)

            if not prediction_sent_for_period.get(next_period, False):
                pred = mega_fusion_engine(history_sides, actual_num)

                streak_emoji = "🔥" if current_streak > 0 else "📉" if current_streak < 0 else "⏸️"
                vote_summary = f"BIG: `{pred['big_votes']}` | SMALL: `{pred['small_votes']}`"

                prediction_msg = (
                    f"🔥 *19 HACKS MEGA FUSION* 🔥\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"🆔 PERIOD: `#{next_period[-5:]}`\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"🎯 PREDICTION: `{pred['prediction']}`\n"
                    f"🔢 TARGET NUMBER: `{pred['number']}`\n"
                    f"⚡ CONFIDENCE: `{pred['confidence']}%`\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"🗳️ *MAJORITY VOTE:*\n"
                    f"{vote_summary}\n"
                    f"📊 Total Votes: `{pred['total_votes']}`\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"{streak_emoji} STREAK: `{current_streak:+d}`\n"
                    f"📈 WIN RATE: `{(total_wins/total_rounds*100) if total_rounds > 0 else 0:.1f}%`\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"⏳ RESULT AWAITING...\n"
                    f"⚡ 19 HACKS MEGA FUSION"
                )

                last_predicted_period = next_period
                last_predicted_signal = pred['prediction']
                last_predicted_num = pred['number']
                prediction_sent_for_period[next_period] = True
                last_result_sent = False

                await send_message(prediction_msg)
                print(f"✅ Prediction: {next_period} → {pred['prediction']} ({pred['number']}) [{pred['big_votes']}B-{pred['small_votes']}S]")

                if len(prediction_sent_for_period) > 10:
                    oldest = min(prediction_sent_for_period.keys())
                    del prediction_sent_for_period[oldest]

        except Exception as e:
            print(f"❌ Loop Error: {e}")
            await asyncio.sleep(5)

# ==================== স্টার্ট ====================
if __name__ == '__main__':
    print("🔥 19 HACKS MEGA FUSION BOT")
    print("━━━━━━━━━━━━━━━━━━━━")
    print(f"📡 TOTAL HACKS: {len(HACKS)}")
    print("🗳️ MAJORITY VOTE SYSTEM")
    print("📊 HOURLY REPORT: ENABLED")
    print("📡 MODE: 1 MIN WINGO")
    print("━━━━━━━━━━━━━━━━━━━━")
    print(f"🤖 BOT: @rakiiibahmed")

    try:
        asyncio.run(prediction_bot())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped")
    except Exception as e:
        print(f"❌ Fatal Error: {e}")
