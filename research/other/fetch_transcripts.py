import os
import subprocess

# 专家及其对应的 YouTube 视频 ID
expert_videos = {
    "Koray_Tugberk_Gubur": "nU7iL9Xn9u8",  # 如果这个还是不行，可以换成 "e-3p_0F_V_8"
    "Aleyda_Solis": "WvOisC9p9_Y",
    "Gael_Breton_AH": "6S8u76_X0f0",
    "Kevin_Indig": "hZf_D7b8R0A"  # 新增一个 Kevin Indig 的视频
}

def download_transcripts():
    base_path = "research/youtube-transcripts"
    
    for author, video_id in expert_videos.items():
        print(f"Starting collection for {author} (ID: {video_id})...")
        try:
            author_dir = os.path.join(base_path, author)
            if not os.path.exists(author_dir):
                os.makedirs(author_dir)
            
            file_path = os.path.join(author_dir, f"{video_id}.txt")
            
            # 使用 subprocess 直接调用命令行工具，绕过代码导入问题
            # 这是最稳健的方法：python -m youtube_transcript_api 视频ID
            result = subprocess.run(
                ["python", "-m", "youtube_transcript_api", video_id],
                capture_output=True,
                text=True,
                encoding="utf-8"
            )
            
            if result.returncode == 0:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(result.stdout)
                print(f"✅ Saved: {file_path}")
            else:
                print(f"❌ Failed {author}: {result.stderr.strip()}")
                
        except Exception as e:
            print(f"❌ Critical Error for {author}: {str(e)}")

if __name__ == "__main__":
    download_transcripts()