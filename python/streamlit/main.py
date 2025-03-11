import streamlit as st

### ファイルアップロード ###
file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
if file:
    st.markdown(f'{file.name} をアップロードしました.')

### プルダウンで選択 ###
uploaded_files = ["file1", "file2", "file3"]
file_names = [file for file in uploaded_files]
# プルダウンメニューでファイル名を選択
selected_file_name = st.selectbox("Select a file", file_names)
