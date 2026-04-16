import os
import subprocess

# 10位SEO专家及其代表性视频ID
expert_videos = {
    "Kevin_Indig": "jxXPpXL2pFg",          # AI SEO Strategy
    "Koray_Tugberk_Gubur": "_U0UQsah3Pc",   # Topical Authority
    "Aleyda_Solis": "ek0yCkmfVuM",          # AI Automation
    "Gael_Breton": "Lt2I-wMGe2Q",        # AI Content Quality
    "Matthew_Woodward": "Qd_c_AwDV6E",      # AI Content Detection
    "Lily_Ray": "2nJkT8zOzcM",              # Google EEAT & AI
    "Bernard_Huang": "o7D0KBb4tAw",         # Information Gain
    "Eli_Schwartz": "EMsfTpSjujk",          # Product-Led SEO
    "Ross_Hudgens": "8-PS7gR2G0I",          # Premium Content AI
    "Kyle_Roof": "frxMhxQXJLc"              # Scientific SEO
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