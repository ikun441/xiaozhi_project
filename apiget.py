from gradio_client import Client, handle_file

client = Client("emilalvaro/E2-F5-TTS", hf_token="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")

# 创建 API 客户端，指定模型地址
client = Client("emilalvaro/E2-F5-TTS")


# 本地参考音频文件路径（需替换为你的文件路径）
local_audio_path = "D:\\PrinterDoctor\\firefly_reference.wav"

# 生成语音的文本
text_to_generate = "生命因何而沉睡？"

# 参考文本（用于模仿音色）
reference_text = "艾利欧能看见未来，他的预言让我知道自己的命运。但我不想被命运完全掌控，我想在既定的命运里，做出自己的选择。就算结局无法改变，我也要在过程中，找到属于自己的意义。"

print('开始调用api!')
# 调用 API 进行语音合成
result = client.predict(
ref_audio_orig=handle_file(local_audio_path), # 上传本地音频文件作为参考音频
ref_text=reference_text, # 参考文本
gen_text=text_to_generate, # 要生成的文本
exp_name="F5-TTS", # 选择 TTS 模型（可选 "F5-TTS" 或 "E2-TTS"）
remove_silence=False, # 是否去除静音（默认 False）
cross_fade_duration=0.15, # 设置交叉淡入淡出时间，默认 0.15 秒
api_name="/infer" # 调用的 API 端点
)


print('已收到数据，解析中……')
# 解析返回结果
synthesized_audio_path = result[0] # 语音文件路径
spectrogram_info = result[1] # 频谱图信息（可选）


print(result) #输出所有信息
# 输出合成语音文件路径
print("合成语音文件路径:",synthesized_audio_path)

# 如果需要，可以自动播放合成的音频（需安装 playsound）
try:
  import playsound
  playsound(synthesized_audio_path) # 播放合成的语音
except ImportError:
  print("如需自动播放音频，请先安装 playsound：pip install playsound")
