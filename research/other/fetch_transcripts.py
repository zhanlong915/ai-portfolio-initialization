import os
import subprocess

# 10位SEO专家及其代表性视频ID
expert_videos = {
    "Kevin_Indig": "hZf_D7b8R0A",          # AI SEO Strategy
    "Koray_Tugberk_Gubur": "e-3p_0F_V_8",   # Topical Authority
    "Aleyda_Solis": "WvOisC9p9_Y",          # AI Automation
    "Gael_Breton_AH": "6S8u76_X0f0",        # AI Content Quality
    "Matthew_Woodward": "pE-DIn9yHWA",      # AI Content Detection
    "Lily_Ray": "Y_6S6GvO_0s",              # Google EEAT & AI
    "Bernard_Huang": "7CAtvV_W2_o",         # Information Gain
    "Eli_Schwartz": "6w_Xp_XwXxw",          # Product-Led SEO
    "Ross_Hudgens": "I4LgZ_z0-3I",          # Premium Content AI
    "Kyle_Roof": "k0n9h76XfXo"              # Scientific SEO
}

def download_transcripts():
    base_path = "research/youtube-transcripts"
    
    for author, video_id in expert_videos.items():
        print(f"--- 正在处理: {author} ---")
        try:
            author_dir = os.path.join(base_path, author)
            if not os.path.exists(author_dir):
                os.makedirs(author_dir)
            
            file_path = os.path.join(author_dir, f"{video_id}.txt")
            
            # 使用 python -m 调用方式保证稳定性
            result = subprocess.run(
                ["python", "-m", "youtube_transcript_api", video_id],
                capture_output=True,
                text=True,
                encoding="utf-8"
            )
            
            if result.returncode == 0:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(result.stdout)
                print(f"✅ 成功抓取并保存")
            else:
                # 如果抓不到，创建一个空的txt，方便你后面手动贴内容
                if not os.path.exists(file_path):
                    open(file_path, 'a').close()
                print(f"⚠️ 无法自动抓取，已创建空文件供后续手动补充内容")
                
        except Exception as e:
            print(f"❌ 运行出错: {str(e)}")

if __name__ == "__main__":
    download_transcripts()