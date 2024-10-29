import streamlit as st
import os
st.markdown(
    """
    <style>
        .main .block-container {
            padding: 0; /* Loại bỏ khoảng cách để chiếm toàn bộ chiều rộng */
            max-width: 80%; /* Chiếm toàn bộ chiều rộng màn hình */
        }
    </style>
    """,
    unsafe_allow_html=True
)
# Tạo tiêu đề cho ứng dụng
st.title("")
st.title("Ứng dụng học tiếng Anh qua hội thoại")

# Lựa chọn hội thoại
dialog_options = ["Hội thoại 1", "Hội thoại 2", "Hội thoại 3"]
selected_dialog = st.selectbox("Chọn hội thoại:", dialog_options)

# Xác định đường dẫn file văn bản và âm thanh theo hội thoại
dialog_num = dialog_options.index(selected_dialog) + 1
eng_file_path = f"data/dialog{dialog_num}_eng.txt"
vi_file_path = f"data/dialog{dialog_num}_vi.txt"
audio_file_path = f"audio/dialog{dialog_num}.wav"

# Trình phát âm thanh
st.subheader("Nghe hội thoại")
if os.path.exists(audio_file_path):
    audio_bytes = open(audio_file_path, 'rb').read()
    st.audio(audio_bytes, format='audio/wav')
else:
    st.write("Âm thanh không có sẵn cho hội thoại này.")

# Hàm đọc nội dung file
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Không tìm thấy file."

# Hiển thị nội dung song ngữ
eng_text = read_file(eng_file_path)
vi_text = read_file(vi_file_path)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Tiếng Anh")
    st.write(eng_text)
with col2:
    st.subheader("Tiếng Việt")
    st.write(vi_text)

