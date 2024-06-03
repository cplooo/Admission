# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
113
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import re
import seaborn as sns
import streamlit as st 
import streamlit.components.v1 as stc 
#os.chdir(r'C:\Users\user\Dropbox\系務\校務研究IR\大一新生學習適應調查分析\112')

# ####### 資料前處理  (建立 'df_admission.pkl')
# ###### 讀入調查結果 
# df_admission = pd.read_excel(r'C:\Users\user\Dropbox\系務\校務研究IR\靜宜大學申請入學甄試服務問卷調查\113\GitHub上傳\result_113.xlsx')
# df_admission.shape  ## (1890, 43)
# df_admission.columns
# df_admission.index  ## RangeIndex(start=0, stop=1890, step=1)
# #df_senior['科系']
# ###### 检查是否有缺失值
# print(df_admission.isna().any().any())  ## True
# df_admission.isna().sum(axis=0) 
# '''
# 請問您的身份 (考生與陪考親友都歡迎填寫) ?                                                 0
# 請問您的高中所在的區域 ?                                                           0
# 請問您的高中學校全名 ?                                                            0
# 請問您今天參與哪些學系甄試(可複選) ?                                                    0
# 請問您今日搭乘的交通工具為何(可複選) ?                                                   0
# 請問您選擇參與靜宜大學申請入學主要原因為何(可複選) ?                                            0
# 參與靜宜大學申請入學「其他」原因描述                                                   1855
# 請問您曾經由哪些管道認識與瞭解靜宜大學(可複選) ?                                              0
# 由哪些管道認識與瞭解靜宜大學「其他」選項描述                                               1871
# 申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?                                  0
# 一階篩選通過學系之聯絡說明，是否會提升您報名參加第二階段甄試之動機 ?                                    49
# 請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?                                       0
# 參加4/20或4/27靜宜大學舉辦之甄試說明會對您瞭解以及選擇學系是否有幫助 ?                              820
# 請描述4/20或4/27甄試說明會對於您瞭解以及選擇學系之幫助為何 ?                                  1010
# 請提供建議: 4/20或4/27甄試說明會對於您瞭解以及選擇學系有何需要改進之處 ?                           1889
# 對於書審資料的準備，你曾經由哪些管道獲得幫助與指引 (可複選，陪考者免填) ?                                 0
# 獲得書審資料的準備指引幫助管道，「其他」選項描述                                             1880
# 請問: 您曾經由哪些管道了解書審資料上傳到甄選會系統的操作步驟(可複選) ?                                  0
# 了解書審資料上傳到甄選會系統的操作步驟之「其他」選項描述                                         1885
# 目前政府對於私立大專校院每年可減免學費3.5萬元，請問: 您知道靜宜大學每學期學費與其他國立大學差距僅約4000-6000元嗎 ?       0
# 請問: 目前教育部的學費補助措施是否會增加您就讀靜宜大學的意願 ?                                       0
# 請問:您知道靜宜大學今年對於各入學管道提供最高達10萬元之獎學金及續領的訊息嗎(詳見靜宜大學網站) ?                     0
# 靜宜大學今年對於各入學管道提供之獎學金訊息是否會增加您就讀靜宜大學的意願 ?                                  0
# 請問您對於本次甄試之【考場指標】的指引是否滿意 ?                                               0
# 對於本次甄試之【考場指標】服務，您(非常)不滿意的原因是什麼 ?                                     1888
# 請問: 您對於本次甄試之【甄試流程】是否滿意 ?                                                0
# 對於本次甄試的【甄試流程】，您(非常)不滿意的原因是什麼 ?                                       1890
# 請問: 您對於本次甄試之【接駁車服務】是否滿意 ?                                               0
# 對於本次甄試的【接駁車服務】，您(非常)不滿意的原因是什麼 ?                                      1890
# 請問: 您對於本次甄試之【服務人員的交通引導(停車或考場位置引導)】是否滿意 ?                                0
# 對於本次甄試的【服務人員的交通引導(停車或考場位置引導)】，您(非常)不滿意的原因是什麼 ?                       1889
# 請問: 您有任何問題或建議嗎 ? 歡迎您提出 !                                             1091
# 請您留下email，本校會再回覆您。                                                    525
# 填答時間                                                                    0
# 填答秒數                                                                    0
# IP紀錄                                                                    0
# 額滿結束註記                                                               1890
# 使用者紀錄                                                                1890
# 會員時間                                                                 1890
# Hash                                                                    0
# 會員編號                                                                    0
# 自訂ID                                                                 1890
# 備註                                                                   1890
# dtype: int64
# ''' 
# # ###### 找出行 '學號' 中含有NA的所有列
# # na_rows = df_senior[df_senior['學號'].isna()]
# # print(na_rows)
# # ###### 删除行 '學號' 中含有NA的所有列
# # df_senior = df_senior.dropna(subset=['學號'])
# # df_senior.shape  ## (1942, 69), 1942 = 1951-9
# # ###### 将行 '學號' 的数据类型更改为字符串 (原為float64)
# # print(df_senior['學號'].dtypes) ## float64
# # df_senior['學號'] = df_senior['學號'].astype(str)
# # print(df_senior['學號'].dtypes) ## object

# # df_senior['畢業院系'].unique()
# # '''
# # array(['國企系', '觀光系', '資傳系', '中文系', '社工系', '法律系', '財工系', '食營系', '企管系',
# #         '應化系', '生態系', '英文系', '日文系', '資碩專班', '資科系(統資系)', '資管系', '台文系',
# #         '西文系', '寰宇外語教育學士學位學程', '財金系', '資工系', '國際碩士學位學程', '寰宇管理學士學位學程',
# #         '教研所', '創新與創業管理碩士學位學程', '社會企業與文化創意碩士學位學程', '會計系', '化科系',
# #         '健康照顧社會工作學士學位學程原住民專班', '大傳系', '法律學士學位學程原住民專班', '管碩專班',
# #         '犯罪防治碩士學位學程', '原住民族文化碩士學位學程'], dtype=object)
# # '''


# ###### 定義系名到學院的映射
# #['Science', 'Management', 'Social','Information','Internation','Language']
# college_map =\
# {'台灣文學系':'人文暨社會科學院', 
#   '中國文學系':'人文暨社會科學院', 
#   '社會工作與兒童少年福利學系':'人文暨社會科學院',  
#   '大眾傳播學系':'人文暨社會科學院', 
#   '法律學系':'人文暨社會科學院', 
#   '生態人文學系':'人文暨社會科學院', 
#   '英國語文學系':'外語學院', 
#   '西班牙語文學系':'外語學院', 
#   '日本語文學系':'外語學院', 
#   '會計學系':'管理學院', 
#   '企業管理學系':'管理學院', 
#   '國際企業學系':'管理學院',
#   '財務金融學系':'管理學院', 
#   '觀光事業學系':'管理學院',
#   '應用化學系':'理學院', 
#   '資料科學暨大數據分析與應用學系(資科系)':'理學院', 
#   '財務工程學系':'理學院',
#   '食品營養學系':'理學院', 
#   '化妝品科學系':'理學院', 
#   '資訊管理學系':'資訊學院', 
#   '資訊工程學系':'資訊學院', 
#   '資訊傳播工程學系':'資訊學院',  
#   '寰宇外語教育學位學士學程':'國際學院', 
#   '寰宇管理學士學位學程':'國際學院', 
# }


# ###### 使用映射來創建新的 '學院別' 欄位
# df_admission.columns
# df_admission['學院'] = df_admission['請問您今天參與哪些學系甄試(可複選) ?'].map(college_map)
# df_admission.shape  ##  (1890, 44)
# # df_admission.head()
# # df_admission.tail(20)

# df_admission_理學 = df_admission[df_admission['學院']=='理學院'].reset_index(drop=True)
# df_admission_資訊 = df_admission[df_admission['學院']=='資訊學院'].reset_index(drop=True)
# df_admission_管理 = df_admission[df_admission['學院']=='管理學院'].reset_index(drop=True)
# df_admission_人社 = df_admission[df_admission['學院']=='人文暨社會科學院'].reset_index(drop=True)
# df_admission_國際 = df_admission[df_admission['學院']=='國際學院'].reset_index(drop=True)
# df_admission_外語 = df_admission[df_admission['學院']=='外語學院'].reset_index(drop=True)
# #df_admission_理學.columns


# ###### 分開 "考生" 與 "陪考親友"
# df_admission_考生 = df_admission[df_admission['請問您的身份 (考生與陪考親友都歡迎填寫) ?']=='考生'].reset_index(drop=True)
# df_admission_考生.shape  ##  (1737, 44)
# df_admission_陪考親友 = df_admission[df_admission['請問您的身份 (考生與陪考親友都歡迎填寫) ?']=='陪考親友'].reset_index(drop=True)
# df_admission_陪考親友.shape  ##  (153, 44)


# ###### 将DataFrame保存为Pickle文件
# df_admission.to_pickle('df_admission_original.pkl')
# ###### 将 DataFrame 保存为 Excel 文件
# df_admission.to_excel('df_admission_original.xlsx', index=False)




####### 定義相關函數 (Part 1)
###### 載入資料
@st.cache_data(ttl=3600, show_spinner="正在加載資料...")  ## Add the caching decorator
def load_data(path):
    df = pd.read_pickle(path)
    return df

###### 計算次數分配並形成 包含'項目', '人數', '比例' 欄位的 dataframe 'result_df'
@st.cache_data(ttl=3600, show_spinner="正在處理資料...")  ## Add the caching decorator
def Frequency_Distribution(df, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1):
    ##### 将字符串按分割符號分割并展平
    split_values = df.iloc[:,column_index].str.split(split_symbol).explode()  ## split_symbol='-'
    #### split_values資料前處理
    ### 去掉每一個字串前後的space
    split_values = split_values.str.strip()
    ### 將以 '其他' 開頭的字串簡化為 '其他'
    split_values_np = np.where(split_values.str.startswith('其他'), '其他', split_values)
    split_values = pd.Series(split_values_np)  ## 轉換為 pandas.core.series.Series
    
    ##### 计算不同子字符串的出现次数
    value_counts = split_values.value_counts()
    #### 去掉 '沒有工讀' index的值:
    if dropped_string in value_counts.index:
        value_counts = value_counts.drop(dropped_string)
        
    ##### 計算總數方式的選擇:
    if sum_choice == 0:    ## 以 "人次" 計算總數
        total_sum = value_counts.sum()
    if sum_choice == 1:    ## 以 "填答人數" 計算總數
        total_sum = df.shape[0]
        
    ##### 计算不同子字符串的比例
    # proportions = value_counts/value_counts.sum()
    proportions = value_counts/total_sum
    
    ##### 轉化為 numpy array
    value_counts_numpy = value_counts.values
    proportions_numpy = proportions.values
    items_numpy = proportions.index.to_numpy()
    
    ##### 创建一个新的DataFrame来显示结果
    result_df = pd.DataFrame({'項目':items_numpy, '人數': value_counts_numpy,'比例': proportions_numpy.round(4)})
    return result_df

###### 調整項目次序
##### 函数：调整 DataFrame 以包含所有項目(以下df['項目']與order的聯集, 實際應用時, df['項目']是order的子集)，且顺序正确(按照以下的order)
@st.cache_data(ttl=3600, show_spinner="正在加載資料...")  ## Add the caching decorator
def adjust_df(df, order):
    # 确保 DataFrame 包含所有滿意度值
    for item in order:
        if item not in df['項目'].values:
            # 创建一个新的 DataFrame，用于添加新的row
            new_row = pd.DataFrame({'項目': [item], '人數': [0], '比例': [0]})
            # 使用 concat() 合并原始 DataFrame 和新的 DataFrame
            df = pd.concat([df, new_row], ignore_index=True)

    # 根据期望的顺序重新排列 DataFrame
    df = df.set_index('項目').reindex(order).reset_index()
    return df




#######  读取Pickle文件
df_admission_original = load_data('df_admission_original.pkl')
# df_admission_original = load_data(r'C:\Users\user\Dropbox\系務\校務研究IR\大一新生學習適應調查分析\112\GitHub上傳\df_freshman_original.pkl')

####### 資料前處理
###### 使用rename方法更改column名称: '請問您今天參與哪些學系甄試(可複選) ?' -> '科系'
df_admission_original = df_admission_original.rename(columns={'請問您今天參與哪些學系甄試(可複選) ?': '科系'})
# df_admission_original.columns

###### '請問您的身份 (考生與陪考親友都歡迎填寫) ?' -> '身分別'
df_admission_original = df_admission_original.rename(columns={'請問您的身份 (考生與陪考親友都歡迎填寫) ?': '身分別'})


###### '資料科學暨大數據分析與應用學系(資科系)' -> '資料科學暨大數據分析與應用學系'
# df_admission_original['科系'] = df_admission_original['科系'].replace('資料科學暨大數據分析與應用學系(資科系)', '資料科學暨大數據分析與應用學系')
# df_admission_original['科系'] = df_admission_original['科系'].apply(lambda x: '資料科學暨大數據分析與應用學系' if '資料科學暨大數據分析與應用學系(資科系)' in x else x)
# df_admission_original['科系'] = df_admission_original['科系'].str.replace('資料科學暨大數據分析與應用學系(資科系)', '資料科學暨大數據分析與應用學系')
# df_admission_original.loc[df_admission_original['科系'].str.contains('資料科學暨大數據分析與應用學系(資科系)', na=False), '科系'] = '資料科學暨大數據分析與應用學系'
# df_admission_original['科系'] = df_admission_original['科系'].str.replace('資料科學暨大數據分析與應用學系(資科系)', '資料科學暨大數據分析與應用學系')
# mask = df_admission_original['科系'].str.contains('資料科學暨大數據分析與應用學系(資科系)')
# df_admission_original.loc[mask, '科系'] = df_admission_original.loc[mask, '科系'].str.replace('資料科學暨大數據分析與應用學系(資科系)', '資料科學暨大數據分析與應用學系')
df_admission_original['科系'] = df_admission_original['科系'].str.replace(r'資料科學暨大數據分析與應用學系\(資科系\)', '資料科學暨大數據分析與應用學系', regex=True)


###### 創造 '學院' 欄位:
college_map =\
{'台灣文學系':'人文暨社會科學院', 
  '中國文學系':'人文暨社會科學院', 
  '社會工作與兒童少年福利學系':'人文暨社會科學院',  
  '大眾傳播學系':'人文暨社會科學院', 
  '法律學系':'人文暨社會科學院', 
  '生態人文學系':'人文暨社會科學院', 
  '英國語文學系':'外語學院', 
  '西班牙語文學系':'外語學院', 
  '日本語文學系':'外語學院', 
  '會計學系':'管理學院', 
  '企業管理學系':'管理學院', 
  '國際企業學系':'管理學院',
  '財務金融學系':'管理學院', 
  '觀光事業學系':'管理學院',
  '應用化學系':'理學院', 
  '資料科學暨大數據分析與應用學系':'理學院', 
  '財務工程學系':'理學院',
  '食品營養學系':'理學院', 
  '化妝品科學系':'理學院', 
  '資訊管理學系':'資訊學院', 
  '資訊工程學系':'資訊學院', 
  '資訊傳播工程學系':'資訊學院',  
  '寰宇外語教育學位學士學程':'國際學院', 
  '寰宇管理學士學位學程':'國際學院', 
}

##### 定義一個函數來根據科系名稱填充學院欄位
def map_colleges(department):
    colleges = []
    for key, value in college_map.items():
        if key in department:
            colleges.append(value)
    return ', '.join(colleges) if colleges else '未知學院'

##### 使用 apply 方法來應用該函數到科系欄位
df_admission_original['學院'] = df_admission_original['科系'].apply(map_colleges)
# set(df_admission_original['學院'])






####### 預先設定
global 系_院_校, choice, df_admission, choice_faculty, df_admission_faculty, selected_options, collections, column_index, dataframes, desired_order, combined_df
###### 預設定院或系之選擇
系_院_校 = '0'
###### 預設定 df_admission 以防止在等待選擇院系輸入時, 發生後面程式df_admission讀不到資料而產生錯誤
choice='財務金融學系' ##
df_admission = df_admission_original[df_admission_original['科系']==choice]
# df_admission.iloc[:,0]
# '''
# 91      考生
# 95      考生
# 105     考生
# 126     考生
# 144     考生
#         ..
# 1581    考生
# 1590    考生
# 1604    考生
# 1611    考生
# 1644    考生
# '''
# choice_faculty = df_admission['學院'][0]  ## 選擇學系所屬學院: '理學院'
choice_faculty = df_admission['學院'].values[0]  ## 選擇學系所屬學院: '管理學院'
df_admission_faculty = df_admission_original[df_admission_original['學院']==choice_faculty]  ## 挑出全校所屬學院之資料
# df_admission_faculty['學院']  

###### 預設定 selected_options, collections
selected_options = ['化妝品科學系','企業管理學系']
# collections = [df_admission_original[df_admission_original['學院']==i] for i in selected_options]
collections = [df_admission_original[df_admission_original['科系']==i] for i in selected_options]
# collections = [df_admission, df_admission_faculty, df_admission_original]
# len(collections) ## 2
# type(collections[0])   ## pandas.core.frame.DataFrame
column_index = 1
dataframes = [Frequency_Distribution(df, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1) for df in collections]  ## 
# len(dataframes)  ## 2
# len(dataframes[1]) ## 5
# len(dataframes[0]) ## 5


##### 形成所有學系'項目'欄位的所有值
desired_order  = list(set([item for df in dataframes for item in df['項目'].tolist()])) 
# desired_order  = list(set([item for item in dataframes[0]['項目'].tolist()])) 

##### 缺的項目值加以擴充， 並統一一樣的項目次序
dataframes = [adjust_df(df, desired_order) for df in dataframes]
# len(dataframes)  ## 2
# len(dataframes[1]) ## 6
# len(dataframes[0]) ## 6, 從原本的5變成6 
# dataframes[0]['項目']
# '''
# 0              體驗生活
# 1         為未來工作累積經驗
# 2             負擔生活費
# 3              增加人脈
# 4    不須負擔生活費但想增加零用錢
# 5         學習應對與表達能力
# Name: 項目, dtype: object
# '''
# dataframes[1]['項目']
# '''
# 0              體驗生活
# 1         為未來工作累積經驗
# 2             負擔生活費
# 3              增加人脈
# 4    不須負擔生活費但想增加零用錢
# 5         學習應對與表達能力
# Name: 項目, dtype: object
# '''
# global combined_df
combined_df = pd.concat(dataframes, keys=selected_options)
# combined_df = pd.concat(dataframes, keys=[choice,choice_faculty,'全校'])
# ''' 
#                           項目  人數      比例
# 化妝品科學系 0       離島 - 金門、連江、澎湖   1  0.0120
#        1     中 - 苗栗、臺中、彰化、南投  36  0.4337
#        2  北 - 臺北、新北、基隆、桃園、新竹  27  0.3253
#        3          中南 - 雲林、嘉義   4  0.0482
#        4        南 - 臺南、高雄、屏東  15  0.1807
# 企業管理學系 0       離島 - 金門、連江、澎湖   1  0.0145
#        1     中 - 苗栗、臺中、彰化、南投  27  0.3913
#        2  北 - 臺北、新北、基隆、桃園、新竹  21  0.3043
#        3          中南 - 雲林、嘉義   5  0.0725
#        4        南 - 臺南、高雄、屏東  15  0.2174
# '''













####### 設定呈現標題 
html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;"> 113靜宜大學申請入學甄試服務問卷調查 </h1>
		</div>
		"""
stc.html(html_temp)
# st.subheader("以下調查與計算母體為大二填答同學1834人")
###### 使用 <h3> 或 <h4> 标签代替更大的标题标签
# st.markdown("##### 以下調查與計算母體為大二填答同學1834人")

###### 或者，使用 HTML 的 <style> 来更精细地控制字体大小和加粗
st.markdown("""
<style>
.bold-small-font {
    font-size:18px !important;
    font-weight:bold !important;
}
</style>
<p class="bold-small-font">以下調查與計算母體為:考生1737人, 陪考親友153人, 共1890人</p>
""", unsafe_allow_html=True)

st.markdown("##")  ## 更大的间隔



st.markdown("""
<style>
.bold-small-font {
    font-size:18px !important;
    font-weight:bold !important;
}
</style>
<p class="bold-small-font">系、院、校 群體選擇 & 填問卷者身份選擇</p>
""", unsafe_allow_html=True)
####### 選擇: 院系 
###### 院 or 系 清單:
departments_list = ['台灣文學系', 
  '中國文學系', 
  '社會工作與兒童少年福利學系',  
  '大眾傳播學系', 
  '法律學系', 
  '生態人文學系', 
  '英國語文學系', 
  '西班牙語文學系', 
  '日本語文學系', 
  '會計學系', 
  '企業管理學系', 
  '國際企業學系',
  '財務金融學系', 
  '觀光事業學系',
  '應用化學系', 
  '資料科學暨大數據分析與應用學系', 
  '財務工程學系',
  '食品營養學系', 
  '化妝品科學系', 
  '資訊管理學系', 
  '資訊工程學系', 
  '資訊傳播工程學系',  
  '寰宇外語教育學位學士學程', 
  '寰宇管理學士學位學程', 
]

faculties_list = ['理學院','資訊學院','管理學院','人文暨社會科學院','外語學院','國際學院']

university_list = ['全校']
university_faculties_list = ['全校','理學院','資訊學院','管理學院','人文暨社會科學院','外語學院','國際學院']

###### 選擇
# 系_院_校 = st.text_input('以學系查詢請輸入 0, 以學院查詢請輸入 1, 以全校查詢請輸入 2 (說明: (i).以學系查詢時同時呈現學院及全校資料. (ii)可以選擇比較單位): ', value='0')
# 系_院_校 = st.text_input('以學系查詢請輸入 0, 學院查詢建置中  (說明: (i).以學系查詢時同時呈現學院及全校資料. (ii)可以選擇比較單位): ', value='0')
系_院_校 = st.text_input('以學系查詢請輸入 0, 以學院查詢請輸入 1, 以全校查詢請輸入 2 (說明: (i)以學系查詢時同時呈現學院及全校資料. (ii)可以選擇比較單位.): ', value='0')


if 系_院_校 == '0':
    # choice = st.selectbox('選擇學系', df_admission_original['科系'].unique())
    choice = st.selectbox('選擇學系', departments_list, index=0)
    #choice = '化科系'
    
    
    
    # df_admission = df_admission_original[df_admission_original['科系']==choice]
    df_admission = df_admission_original[df_admission_original['科系'].str.contains(choice, regex=True)]
    # df_admission_whole = df_admission
          
    # choice_faculty = df_admission['學院'].values[0]  ## 選擇學系所屬學院
    choice_faculty = college_map[choice]
    df_admission_faculty = df_admission_original[df_admission_original['學院'].str.contains(choice_faculty, regex=True)]  ## 挑出全校所屬學院之資料
    # df_admission_faculty_whole = df_admission_faculty

    # selected_options = st.multiselect('選擇比較學系：', df_freshman_original['科系'].unique(), default=['化科系','企管系'])
    # selected_options = ['化科系','企管系']
    # collections = [df_freshman_original[df_freshman_original['科系']==i] for i in selected_options]
    # dataframes = [Frequency_Distribution(df, 7) for df in collections]
    # combined_df = pd.concat(dataframes, keys=selected_options)
    # #### 去掉 level 1 index
    # combined_df_r = combined_df.reset_index(level=1, drop=True)
elif 系_院_校 == '1':
    # choice = st.selectbox('選擇學院', df_admission_original['學院'].unique(),index=0)
    choice = st.selectbox('選擇學院', faculties_list, index=0)
    #choice = '管理'
    # df_admission = df_admission_original[df_admission_original['學院']==choice]
    df_admission = df_admission_original[df_admission_original['學院'].str.contains(choice, regex=True)]  ## ## 沒有用途, 只是為了不要讓 Draw() 中的參數 'df_admission' 缺漏
    # df_admission_whole = df_admission
    # df_admission_faculty_whole = df_admission   ## 沒有用途, 只是為了不要讓 Draw() 中的參數 'df_admission_faculty' 缺漏
    df_admission_faculty = df_admission   ## 沒有用途, 只是為了不要讓 Draw() 中的參數 'df_admission_faculty' 缺漏
    # selected_options = st.multiselect('選擇比較學的院：', df_freshman_original['學院'].unique(), default=['理學院','資訊學院'])
    # collections = [df_freshman_original[df_freshman_original['學院']==i] for i in selected_options]
    # dataframes = [Frequency_Distribution(df, 7) for df in collections]
    # combined_df = pd.concat(dataframes, keys=selected_options)
elif 系_院_校 == '2':
    choice = '全校'
    # choice = st.selectbox('選擇:全校', university_list, index=0)
    # if choice !='全校':
    #     df_admission = df_admission_original[df_admission_original['學院'].str.contains(choice, regex=True)]
    # if choice !='全校':
    #     df_admission = df_admission_original
    
    df_admission = df_admission_original  ## 沒有用途, 只是為了不要讓 Draw() 中的參數 'df_admission' 缺漏
    df_admission_faculty = df_admission  ## 沒有用途, 只是為了不要讓 Draw() 中的參數 'df_admission_faculty' 缺漏


df_streamlit = []
column_title = []

####### 選擇身分別  (要放在 Q1 之後)
考生or親友or全部_list = ['考生','陪考親友','全部']
考生or親友or全部 = st.selectbox('選擇想獲取的資訊之身份別(考生,陪考親友,全部)', 考生or親友or全部_list)
st.markdown("##")  ## 更大的间隔





####### 定義相關函數 (Part 2): 因為函數 'Draw' 的定義需要使用 'dataframes','combined_df' 來進行相關計算, 因此要放在以上 '預先設定' 之後才會有 'dataframes', 'combined_df' 的值
###### 畫圖形(單一學系或學院, 比較圖形)
@st.cache_data(ttl=3600, show_spinner="正在處理資料...")  ## Add the caching decorator
def Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=pd.DataFrame(), selected_options=[], dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 14,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name='', rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty, desired_order=desired_order):
    ##### 使用Streamlit畫單一圖
    if 系_院_校 == '0':
        collections = [df_admission, df_admission_faculty, df_admission_original]
        if rank == True:
            dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice).head(rank_number) for df in collections]  ## 'dataframes' list 中的各dataframe已經是按照次數高至低的項目順序排列
        else:
            dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice) for df in collections]  ## 'dataframes' list 中的各dataframe已經是按照次數高至低的項目順序排列
        ## 形成所有學系'項目'欄位的所有值
        # desired_order  = list(set([item for df in dataframes for item in df['項目'].tolist()]))
        # desired_order  = list(set([item for item in dataframes[0]['項目'].tolist()])) 
        #### 只看所選擇學系的項目(已經是按照次數高至低的項目順序排列), 並且反轉次序使得表與圖的項目次序一致
        desired_order  = [item for item in dataframes[0]['項目'].tolist()]  ## 只看所選擇學系的項目
        desired_order = desired_order[::-1]  ## 反轉次序使得表與圖的項目次序一致
        ## 缺的項目值加以擴充， 並統一一樣的項目次序
        dataframes = [adjust_df(df, desired_order) for df in dataframes]
        combined_df = pd.concat(dataframes, keys=[choice,choice_faculty,'全校'])
        # 获取level 0索引的唯一值并保持原始顺序
        unique_level0 = combined_df.index.get_level_values(0).unique()

        #### 設置 matplotlib 支持中文的字體: 
        # matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
        # matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
        # matplotlib.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
        matplotlib.rcParams['font.family'] = 'Noto Sans CJK JP'
        matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        #### 设置条形的宽度
        # bar_width = 0.2
        #### 设置y轴的位置
        r = np.arange(len(dataframes[0]))  ## len(result_df_理學_rr)=6, 因為result_df_理學_rr 有 6個 row: 非常滿意, 滿意, 普通, 不滿意, 非常不滿意
        # #### 设置字体大小
        # title_fontsize = title_fontsize ##15
        # xlabel_fontsize = xlabel_fontsize  ##14
        # ylabel_fontsize = ylabel_fontsize  ##14
        # xticklabel_fontsize = 14
        # yticklabel_fontsize = 14
        # annotation_fontsize = 8
        # legend_fontsize = legend_fontsize  ##14
        #### 绘制条形
        fig, ax = plt.subplots(figsize=(width1, heigh1))
        # for i, (college_name, df) in enumerate(combined_df.groupby(level=0)):
        for i, college_name in enumerate(unique_level0):            
            df = combined_df.loc[college_name]
            # 计算当前分组的条形数量
            num_bars = len(df)
            # 生成当前分组的y轴位置
            index = np.arange(num_bars) + i * bar_width
            # index = r + i * bar_width
            rects = ax.barh(index, df['比例'], height=bar_width, label=college_name)
    
            # # 在每个条形上标示比例
            # for rect, ratio in zip(rects, df['比例']):
            #     ax.text(rect.get_x() + rect.get_width() / 2.0, rect.get_height(), f'{ratio:.1%}', ha='center', va='bottom',fontsize=annotation_fontsize)
        ### 添加图例
        if fontsize_adjust==0:
            ax.legend()
        if fontsize_adjust==1:
            ax.legend(fontsize=legend_fontsize)

        # ### 添加x轴标签
        # ## 计算每个组的中心位置作为x轴刻度位置
        # # group_centers = r + bar_width * (num_colleges / 2 - 0.5)
        # # group_centers = np.arange(len(dataframes[0]))
        # ## 添加x轴标签
        # # ax.set_xticks(group_centers)
        # # dataframes[0]['項目'].values
        # # "array(['個人興趣', '未來能找到好工作', '落點分析', '沒有特定理由', '家人的期望與建議', '師長推薦'],dtype=object)"
        # ax.set_xticks(r + bar_width * (len(dataframes) / 2))
        # ax.set_xticklabels(dataframes[0]['項目'].values, fontsize=xticklabel_fontsize)
        # # ax.set_xticklabels(['非常滿意', '滿意', '普通', '不滿意','非常不滿意'],fontsize=xticklabel_fontsize)
        
        ### 设置x,y轴刻度标签
        ax.set_yticks(r + bar_width*(len(dataframes) / 2))  # 调整位置以使标签居中对齐到每个条形
        if fontsize_adjust==0:
            ax.set_yticklabels(dataframes[0]['項目'].values)
            ax.tick_params(axis='x')
        if fontsize_adjust==1:
            ax.set_yticklabels(dataframes[0]['項目'].values, fontsize=yticklabel_fontsize)
            ## 设置x轴刻度的字体大小
            ax.tick_params(axis='x', labelsize=xticklabel_fontsize)
        # ax.set_yticklabels(dataframes[0]['項目'].values)
        # ax.set_yticklabels(dataframes[0]['項目'].values, fontsize=yticklabel_fontsize)


        ### 设置标题和轴标签
        if fontsize_adjust==0:
            ax.set_title(item_name)
        if fontsize_adjust==1:
            ax.set_title(item_name,fontsize=title_fontsize)
        
        # ax.set_xlabel('满意度',fontsize=xlabel_fontsize)
        if fontsize_adjust==0:
            ax.set_xlabel('比例')
        if fontsize_adjust==1:
            ax.set_xlabel('比例',fontsize=xlabel_fontsize)
        
        ### 显示网格线
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.tight_layout()
        # plt.show()
        ### 在Streamlit中显示
        st.pyplot(plt)

    if 系_院_校 == '1':
    # else:  ## 包含 系_院_校 == '1', 系_院_校 == '2'
        #### 設置中文顯示
        # matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
        # matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
        matplotlib.rcParams['font.family'] = 'Noto Sans CJK JP'
        matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        #### 创建图形和坐标轴
        plt.figure(figsize=(width2, heigh2))
        #### 绘制条形图
        ### 反轉 dataframe result_df 的所有行的值的次序,  使得表與圖的項目次序一致
        result_df = result_df.iloc[::-1].reset_index(drop=True)
        if rank == True:
            result_df = result_df.head(rank_number)

        # plt.barh(result_df['項目'], result_df['人數'], label=choice, width=bar_width)
        plt.barh(result_df['項目'], result_df['人數'], label=choice)
        #### 標示比例數據
        for i in range(len(result_df['項目'])):
            if fontsize_adjust==0:
                plt.text(result_df['人數'][i]+1, result_df['項目'][i], f'{result_df.iloc[:, 2][i]:.1%}')
            if fontsize_adjust==1:
                plt.text(result_df['人數'][i]+1, result_df['項目'][i], f'{result_df.iloc[:, 2][i]:.1%}', fontsize=annotation_fontsize)
            
        #### 添加一些图形元素
        if fontsize_adjust==0:
            plt.title(item_name)
            plt.xlabel('人數')
        if fontsize_adjust==1:
            plt.title(item_name, fontsize=title_fontsize)
            plt.xlabel('人數', fontsize=xlabel_fontsize)
        
        #plt.ylabel('本校現在所提供的資源或支援事項')
        #### 调整x轴和y轴刻度标签的字体大小
        if fontsize_adjust==0:
            # plt.tick_params(axis='both')
            ## 设置x轴刻度的字体大小
            plt.tick_params(axis='x')
            ## 设置y轴刻度的字体大小
            plt.tick_params(axis='y')
        if fontsize_adjust==1:
            # plt.tick_params(axis='both', labelsize=xticklabel_fontsize)  # 同时调整x轴和y轴 
            ## 设置x轴刻度的字体大小
            plt.tick_params(axis='x', labelsize=xticklabel_fontsize)
            ## 设置y轴刻度的字体大小
            plt.tick_params(axis='y', labelsize=yticklabel_fontsize)
        
        if fontsize_adjust==0:
            plt.legend()
        if fontsize_adjust==1:
            plt.legend(fontsize=legend_fontsize)
        
        #### 显示网格线
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        #### 显示图形
        ### 一般顯示
        # plt.show()
        ### 在Streamlit中显示
        st.pyplot(plt)
        
    if 系_院_校 == '2':
    # else:  ## 包含 系_院_校 == '1', 系_院_校 == '2'
        #### 設置中文顯示
        # matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
        # matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
        matplotlib.rcParams['font.family'] = 'Noto Sans CJK JP'
        matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        #### 创建图形和坐标轴
        plt.figure(figsize=(width2, heigh2))
        #### 绘制条形图
        ### 反轉 dataframe result_df 的所有行的值的次序,  使得表與圖的項目次序一致
        result_df = result_df.iloc[::-1].reset_index(drop=True)
        if rank == True:
            result_df = result_df.head(rank_number)

        # plt.barh(result_df['項目'], result_df['人數'], label=choice, width=bar_width)
        plt.barh(result_df['項目'], result_df['人數'], label=choice)
        #### 標示比例數據
        for i in range(len(result_df['項目'])):
            if fontsize_adjust==0:
                plt.text(result_df['人數'][i]+1, result_df['項目'][i], f'{result_df.iloc[:, 2][i]:.1%}')
            if fontsize_adjust==1:
                plt.text(result_df['人數'][i]+1, result_df['項目'][i], f'{result_df.iloc[:, 2][i]:.1%}', fontsize=annotation_fontsize)
            
        #### 添加一些图形元素
        if fontsize_adjust==0:
            plt.title(item_name)
            plt.xlabel('人數')
        if fontsize_adjust==1:
            plt.title(item_name, fontsize=title_fontsize)
            plt.xlabel('人數', fontsize=xlabel_fontsize)
        
        #plt.ylabel('本校現在所提供的資源或支援事項')
        #### 调整x轴和y轴刻度标签的字体大小
        if fontsize_adjust==0:
            # plt.tick_params(axis='both')
            ## 设置x轴刻度的字体大小
            plt.tick_params(axis='x')
            ## 设置y轴刻度的字体大小
            plt.tick_params(axis='y')
        if fontsize_adjust==1:
            # plt.tick_params(axis='both', labelsize=xticklabel_fontsize)  # 同时调整x轴和y轴 
            ## 设置x轴刻度的字体大小
            plt.tick_params(axis='x', labelsize=xticklabel_fontsize)
            ## 设置y轴刻度的字体大小
            plt.tick_params(axis='y', labelsize=yticklabel_fontsize)
        
        if fontsize_adjust==0:
            plt.legend()
        if fontsize_adjust==1:
            plt.legend(fontsize=legend_fontsize)
        
        #### 显示网格线
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        #### 显示图形
        ### 一般顯示
        # plt.show()
        ### 在Streamlit中显示
        st.pyplot(plt)



    ##### 使用streamlit 畫比較圖 (全校的群體不會畫出比較圖)
    # st.subheader("不同單位比較")
    ### 系或院群體才會畫比較圖:
    if 系_院_校 == '0' or '1' or '2':
        if 系_院_校 == '0':
            collections = [df_admission_original[df_admission_original['科系'].str.contains(i, regex=True)] for i in selected_options]
            
            if rank == True:
                dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice).head(rank_number) for df in collections]  ## 'dataframes' list 中的各dataframe已經是按照次數高至低的項目順序排列
            else:
                dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice) for df in collections]
    
    
            # #### 只看第一個選擇學系的項目(已經是按照次數高至低的項目順序排列), 並且反轉次序使得表與圖的項目次序一致
            # desired_order  = [item for item in dataframes[0]['項目'].tolist()]  ## 只看第一個選擇學系的項目
            # desired_order = desired_order[::-1]  ## 反轉次序使得表與圖的項目次序一致
            ## 形成所有學系'項目'欄位的所有值
            # desired_order  = list(set([item for df in dataframes for item in df['項目'].tolist()])) 
            desired_order  = list(dict.fromkeys([item for df in dataframes for item in df['項目'].tolist()]))

            ## 缺的項目值加以擴充， 並統一一樣的項目次序
            dataframes = [adjust_df(df, desired_order) for df in dataframes]
            combined_df = pd.concat(dataframes, keys=selected_options)
        elif 系_院_校 == '1':
            collections = [df_admission_original[df_admission_original['學院'].str.contains(i, regex=True)] for i in selected_options]
            
            if rank == True:
                dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice).head(rank_number) for df in collections]  ## 'dataframes' list 中的各dataframe已經是按照次數高至低的項目順序排列
            else:
                dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice) for df in collections]
    
            
            ## 形成所有學系'項目'欄位的所有值
            # desired_order  = list(set([item for df in dataframes for item in df['項目'].tolist()])) 
            desired_order  = list(dict.fromkeys([item for df in dataframes for item in df['項目'].tolist()]))
            ## 缺的項目值加以擴充， 並統一一樣的項目次序
            dataframes = [adjust_df(df, desired_order) for df in dataframes]        
            combined_df = pd.concat(dataframes, keys=selected_options)
        elif 系_院_校 == '2':
            # collections = [df_admission_original[df_admission_original['學院'].str.contains(i, regex=True)] for i in selected_options if i!='全校' else df_admission_original]
            # collections = [df_admission_original] + collections
            collections = [df_admission_original if i == '全校' else df_admission_original[df_admission_original['學院'].str.contains(i, regex=True)] for i in selected_options]

            
            if rank == True:
                dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice).head(rank_number) for df in collections]  ## 'dataframes' list 中的各dataframe已經是按照次數高至低的項目順序排列
            else:
                dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice) for df in collections]
        
                
            ## 形成所有學系'項目'欄位的所有值
            # desired_order  = list(set([item for df in dataframes for item in df['項目'].tolist()])) 
            desired_order  = list(dict.fromkeys([item for df in dataframes for item in df['項目'].tolist()]))
            # desired_order = desired_order[::-1]  ## 反轉次序使得表與圖的項目次序一致
            ## 缺的項目值加以擴充， 並統一一樣的項目次序
            dataframes = [adjust_df(df, desired_order) for df in dataframes]        
            combined_df = pd.concat(dataframes, keys=selected_options)
            # combined_df = pd.concat(dataframes, keys=['全校'])

            
        # 获取level 0索引的唯一值并保持原始顺序
        unique_level0 = combined_df.index.get_level_values(0).unique()
    
        #### 設置 matplotlib 支持中文的字體: 
        # matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
        # matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
        # matplotlib.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
        matplotlib.rcParams['font.family'] = 'Noto Sans CJK JP'
        matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        # #### 设置条形的宽度
        # bar_width = 0.2
        #### 设置y轴的位置
        # r = np.arange(len(dataframes[0]))  ## len(result_df_理學_rr)=6, 因為result_df_理學_rr 有 6個 row: 非常滿意, 滿意, 普通, 不滿意, 非常不滿意
        r = np.arange(len(desired_order))
        # #### 设置字体大小
        # title_fontsize = 15
        # xlabel_fontsize = 14
        # ylabel_fontsize = 14
        # xticklabel_fontsize = 14
        # yticklabel_fontsize = 14
        # annotation_fontsize = 8
        # legend_fontsize = 14
        
    
        #### 绘制条形
        fig, ax = plt.subplots(figsize=(width3, heigh3))
        # if 系_院_校 == '0' or '1':
        # for i, (college_name, df) in enumerate(combined_df.groupby(level=0)):
        for i, college_name in enumerate(unique_level0):            
            df = combined_df.loc[college_name]
            # 计算当前分组的条形数量
            num_bars = len(df)
            # 生成当前分组的y轴位置
            index = np.arange(num_bars) + i * bar_width
            # index = r + i * bar_width
            # if 系_院_校 == '0' or '1':
            rects = ax.barh(index, df['比例'], height=bar_width, label=college_name)
        # if 系_院_校 == '2':
        # #     index = np.arange(len(desired_order))
        # #     rects = ax.barh(index, dataframes[0]['比例'], height=bar_width, label='全校')
        #     for i, college_name in enumerate(unique_level0):            
        #         df = combined_df.loc[college_name]
        #         # 计算当前分组的条形数量
        #         num_bars = len(df)
        #         # 生成当前分组的y轴位置
        #         index = np.arange(num_bars) + i * bar_width
        #         # index = r + i * bar_width
        #         # if 系_院_校 == '0' or '1':
        #         # rects = ax.barh(index, df['比例'], height=bar_width, label='全校')
        #         # if i==0:
        #         rects = ax.barh(index, df['比例'], height=bar_width, label=college_name)
        
    
            # # 在每个条形上标示比例
            # for rect, ratio in zip(rects, df['比例']):
            #     ax.text(rect.get_x() + rect.get_width() / 2.0, rect.get_height(), f'{ratio:.1%}', ha='center', va='bottom',fontsize=annotation_fontsize)
        
        # if 系_院_校 == '0' or '1':
        ### 添加图例
        if fontsize_adjust==0:
            ax.legend()
        if fontsize_adjust==1:
            ax.legend(fontsize=legend_fontsize)
        
    
        # ### 添加x轴标签
        # ## 计算每个组的中心位置作为x轴刻度位置
        # # group_centers = r + bar_width * (num_colleges / 2 - 0.5)
        # # group_centers = np.arange(len(dataframes[0]))
        # ## 添加x轴标签
        # # ax.set_xticks(group_centers)
        # # dataframes[0]['項目'].values
        # # "array(['個人興趣', '未來能找到好工作', '落點分析', '沒有特定理由', '家人的期望與建議', '師長推薦'],dtype=object)"
        # ax.set_xticks(r + bar_width * (len(dataframes) / 2))
        # ax.set_xticklabels(dataframes[0]['項目'].values, fontsize=xticklabel_fontsize)
        # # ax.set_xticklabels(['非常滿意', '滿意', '普通', '不滿意','非常不滿意'],fontsize=xticklabel_fontsize)
    
        ### 设置x,y轴刻度标签
        ax.set_yticks(r + bar_width*(len(dataframes) / 2))  # 调整位置以使标签居中对齐到每个条形
        if fontsize_adjust==0:
            # ax.set_yticklabels(dataframes[0]['項目'].values) 
            ax.set_yticklabels(desired_order)
            ax.tick_params(axis='x')
        if fontsize_adjust==1:
            # ax.set_yticklabels(dataframes[0]['項目'].values, fontsize=yticklabel_fontsize)
            ax.set_yticklabels(desired_order, fontsize=yticklabel_fontsize)
            ## 设置x轴刻度的字体大小
            ax.tick_params(axis='x', labelsize=xticklabel_fontsize)
            
        
    
    
        ### 设置标题和轴标签
        if fontsize_adjust==0:
            ax.set_title(item_name)
            ax.set_xlabel('比例')
        if fontsize_adjust==1:
            ax.set_title(item_name,fontsize=title_fontsize)
            ax.set_xlabel('比例',fontsize=xlabel_fontsize)
        
        
        
        ### 显示网格线
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.tight_layout()
        # plt.show()
        ### 在Streamlit中显示
        # if 系_院_校 == '0' or '1':
        st.pyplot(plt)


        




###### 畫圖形(比較兩種群體圖形: df_admission_restrict, df_admission )
@st.cache_data(ttl=3600, show_spinner="正在處理資料...")  ## Add the caching decorator
# def Draw_2(院_系, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=pd.DataFrame(), selected_options=[], dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 14,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name='', rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty):
def Draw_2(column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 14,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name='', rank=False, rank_number=5, df_admission=df_admission, df_admission_restrict=df_admission):

    collections = [df_admission_restrict, df_admission]
    if rank == True:
        dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice).head(rank_number) for df in collections]  ## 'dataframes' list 中的各dataframe已經是按照次數高至低的項目順序排列
    else:
        dataframes = [Frequency_Distribution(df, column_index, split_symbol, dropped_string, sum_choice) for df in collections]  ## 'dataframes' list 中的各dataframe已經是按照次數高至低的項目順序排列
    ## 形成所有學系'項目'欄位的所有值
    # desired_order  = list(set([item for df in dataframes for item in df['項目'].tolist()]))
    # desired_order  = list(set([item for item in dataframes[0]['項目'].tolist()])) 
    #### 只看所選擇學系的項目(已經是按照次數高至低的項目順序排列), 並且反轉次序使得表與圖的項目次序一致
    desired_order  = [item for item in dataframes[0]['項目'].tolist()]  ## 只看所選擇學系的項目
    desired_order = desired_order[::-1]  ## 反轉次序使得表與圖的項目次序一致
    ## 缺的項目值加以擴充， 並統一一樣的項目次序
    dataframes = [adjust_df(df, desired_order) for df in dataframes]
    combined_df = pd.concat(dataframes, keys=['重點高中','所有高中'])
    # 获取level 0索引的唯一值并保持原始顺序
    unique_level0 = combined_df.index.get_level_values(0).unique()

    #### 設置 matplotlib 支持中文的字體: 
    # matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
    # matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # matplotlib.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
    matplotlib.rcParams['font.family'] = 'Noto Sans CJK JP'
    matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    #### 设置条形的宽度
    # bar_width = 0.2
    #### 设置y轴的位置
    r = np.arange(len(dataframes[0]))  ## len(result_df_理學_rr)=6, 因為result_df_理學_rr 有 6個 row: 非常滿意, 滿意, 普通, 不滿意, 非常不滿意
    # #### 设置字体大小
    # title_fontsize = title_fontsize ##15
    # xlabel_fontsize = xlabel_fontsize  ##14
    # ylabel_fontsize = ylabel_fontsize  ##14
    # xticklabel_fontsize = 14
    # yticklabel_fontsize = 14
    # annotation_fontsize = 8
    # legend_fontsize = legend_fontsize  ##14
    #### 绘制条形
    fig, ax = plt.subplots(figsize=(width1, heigh1))
    # for i, (college_name, df) in enumerate(combined_df.groupby(level=0)):
    for i, college_name in enumerate(unique_level0):            
        df = combined_df.loc[college_name]
        # 计算当前分组的条形数量
        num_bars = len(df)
        # 生成当前分组的y轴位置
        index = np.arange(num_bars) + i * bar_width
        # index = r + i * bar_width
        rects = ax.barh(index, df['比例'], height=bar_width, label=college_name)

        # # 在每个条形上标示比例
        # for rect, ratio in zip(rects, df['比例']):
        #     ax.text(rect.get_x() + rect.get_width() / 2.0, rect.get_height(), f'{ratio:.1%}', ha='center', va='bottom',fontsize=annotation_fontsize)
    ### 添加图例
    if fontsize_adjust==0:
        ax.legend()
    if fontsize_adjust==1:
        ax.legend(fontsize=legend_fontsize)

    # ### 添加x轴标签
    # ## 计算每个组的中心位置作为x轴刻度位置
    # # group_centers = r + bar_width * (num_colleges / 2 - 0.5)
    # # group_centers = np.arange(len(dataframes[0]))
    # ## 添加x轴标签
    # # ax.set_xticks(group_centers)
    # # dataframes[0]['項目'].values
    # # "array(['個人興趣', '未來能找到好工作', '落點分析', '沒有特定理由', '家人的期望與建議', '師長推薦'],dtype=object)"
    # ax.set_xticks(r + bar_width * (len(dataframes) / 2))
    # ax.set_xticklabels(dataframes[0]['項目'].values, fontsize=xticklabel_fontsize)
    # # ax.set_xticklabels(['非常滿意', '滿意', '普通', '不滿意','非常不滿意'],fontsize=xticklabel_fontsize)
    
    ### 设置x,y轴刻度标签
    ax.set_yticks(r + bar_width*(len(dataframes) / 2))  # 调整位置以使标签居中对齐到每个条形
    if fontsize_adjust==0:
        ax.set_yticklabels(dataframes[0]['項目'].values)
        ax.tick_params(axis='x')
    if fontsize_adjust==1:
        ax.set_yticklabels(dataframes[0]['項目'].values, fontsize=yticklabel_fontsize)
        ## 设置x轴刻度的字体大小
        ax.tick_params(axis='x', labelsize=xticklabel_fontsize)
    # ax.set_yticklabels(dataframes[0]['項目'].values)
    # ax.set_yticklabels(dataframes[0]['項目'].values, fontsize=yticklabel_fontsize)


    ### 设置标题和轴标签
    if fontsize_adjust==0:
        ax.set_title(item_name)
    if fontsize_adjust==1:
        ax.set_title(item_name,fontsize=title_fontsize)
    
    # ax.set_xlabel('满意度',fontsize=xlabel_fontsize)
    if fontsize_adjust==0:
        ax.set_xlabel('比例')
    if fontsize_adjust==1:
        ax.set_xlabel('比例',fontsize=xlabel_fontsize)
    
    ### 显示网格线
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    plt.tight_layout()
    # plt.show()
    ### 在Streamlit中显示
    st.pyplot(plt)







####### 問卷的各項問題
st.markdown("""
<style>
.bold-small-font {
    font-size:18px !important;
    font-weight:bold !important;
}
</style>
<p class="bold-small-font">基本資料</p>
""", unsafe_allow_html=True)


###### 身分別
with st.expander("Q1. 身分別(考生與陪考親友的佔比):"):
    # df_admission.iloc[:,0] ## 0 身分別
    column_index = 0
    item_name = "身分別(考生與陪考親友的佔比)"
    column_title.append(df_admission.columns[column_index][0:])


    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)

    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    #### 畫比較圖時, 比較單位之選擇:
    if 系_院_校 == '0':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
        selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    if 系_院_校 == '1':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
        selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')
    if 系_院_校 == '2':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
        selected_options = st.multiselect('選擇: 全校 or 各院：', university_faculties_list, default=['全校','理學院'],key=str(column_index)+'university')




    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 16, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



# ####### 選擇身分別  (要放在 Q1 之後)
# 考生or親友or全部_list = ['考生','陪考親友','全部']
# 考生or親友or全部 = st.selectbox('選擇想獲取的資訊之身份別(考生,陪考親友,全部)', 考生or親友or全部_list)
## '0', '1' , '2' 都相同
if 系_院_校 == '0':
    if 考生or親友or全部 == '考生':
        df_admission = df_admission[df_admission['身分別']=='考生'] 
    if 考生or親友or全部 == '陪考親友':
        df_admission = df_admission[df_admission['身分別']=='陪考親友'] 
    if 考生or親友or全部 == '全部':
        df_admission = df_admission 
if 系_院_校 == '1':
    if 考生or親友or全部 == '考生':
        df_admission = df_admission[df_admission['身分別']=='考生'] 
    if 考生or親友or全部 == '陪考親友':
        df_admission = df_admission[df_admission['身分別']=='陪考親友'] 
    if 考生or親友or全部 == '全部':
        df_admission = df_admission
if 系_院_校 == '2':
    if 考生or親友or全部 == '考生':
        df_admission = df_admission[df_admission['身分別']=='考生'] 
    if 考生or親友or全部 == '陪考親友':
        df_admission = df_admission[df_admission['身分別']=='陪考親友'] 
    if 考生or親友or全部 == '全部':
        df_admission = df_admission 

  


###### 高中位置
with st.expander("Q2. 高中位置:"):
    # df_admission.iloc[:,0] ## 0 身分別
    column_index = 1
    item_name = "高中位置"
    column_title.append(df_admission.columns[column_index][0:])


    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)

    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    #### 畫比較圖時, 比較單位之選擇:
    if 系_院_校 == '0':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
        selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    if 系_院_校 == '1':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
        selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')
    if 系_院_校 == '2':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
        selected_options = st.multiselect('選擇: 全校 or 各院：', university_faculties_list, default=['全校','理學院'],key=str(column_index)+'university')




    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 16,legend_fontsize = 18,xticklabel_fontsize = 16, yticklabel_fontsize = 16, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 高中別
with st.expander("Q3. 高中別:"):
    # df_admission.iloc[:,0] ## 0 身分別
    column_index = 2
    item_name = "高中別(前 5大)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)    
    #### 選取前面 5 筆資料
    result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    #### 畫比較圖時, 比較單位之選擇:
    if 系_院_校 == '0':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
        selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    if 系_院_校 == '1':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
        selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')
    if 系_院_校 == '2':
        ## 使用multiselect组件让用户进行多重选择
        # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
        selected_options = st.multiselect('選擇: 全校 or 各院：', university_faculties_list, default=['全校','理學院'],key=str(column_index)+'university')


    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=True, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 





# ###### 各學系填答人數與比例
# with st.expander("Q4. 各學系填答人數與比例:"):
#     # df_admission.iloc[:,0] ## 0 身分別
#     column_index = 3
#     item_name = "各學系填答人數與比例"
#     column_title.append(df_admission.columns[column_index][0:])
#     # set(df_admission_original['科系'])

#     ##### 產出 result_df
#     result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)

#     ##### 存到 list 'df_streamlit'
#     df_streamlit.append(result_df)  

#     ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
#     # st.write(choice)
#     st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
#     st.write(result_df.to_html(index=False), unsafe_allow_html=True)
#     st.markdown("##")  ## 更大的间隔

#     ##### 使用Streamlit畫單一圖 & 比較圖
#     #### 畫比較圖時, 比較單位之選擇:
#     if 系_院_校 == '0':
#         ## 使用multiselect组件让用户进行多重选择
#         # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
#         selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
#     if 系_院_校 == '1':
#         ## 使用multiselect组件让用户进行多重选择
#         # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
#         selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

#     # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
#     # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
#     Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 14,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name=item_name)    
    
# st.markdown("##")  ## 更大的间隔



###### 各學系填答人數與比例
with st.expander("Q4. 各學系填答人數與比例(複選): 報考所選擇單位(系院校)之學系考生, 其重複報考各學系分佈情形."):
    # df_admission.iloc[:,3] ## 
    column_index = 3
    item_name = "在所選擇的群體中, 各學系填答人數與比例(複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 16, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔  



###### 今日搭乘的交通工具(可複選)
with st.expander("Q5. 今日搭乘的交通工具(可複選):"):
    # df_admission.iloc[:,4] ## 
    column_index = 4
    item_name = "今日搭乘的交通工具(可複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 16, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔  



st.markdown("""
<style>
.bold-small-font {
    font-size:18px !important;
    font-weight:bold !important;
}
</style>
<p class="bold-small-font">申請入學相關</p>
""", unsafe_allow_html=True)
###### 參與靜宜大學申請入學主要原因(複選)
with st.expander("Q6. 參與靜宜大學申請入學主要原因(複選):"):
    # df_admission.iloc[:,5] ## 
    column_index = 5
    item_name = "參與靜宜大學申請入學主要原因(複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 16, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=0, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 特定高中參與靜宜大學申請入學主要原因(複選)
with st.expander("Q6-特定高中. 特定高中參與靜宜大學申請入學主要原因(複選):"):
    # df_admission.iloc[:,5] ## 
    column_index = 5
    # item_name = "特定高中參與靜宜大學申請入學主要原因(複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5
    highlight_schools = ['清水高中','龍津高中','中港高中','弘文高中','新民高中','僑泰高中','立人高中']
    selected_options = st.multiselect('選擇重點高中：', highlight_schools, default=['清水高中','龍津高中'],key='highlight_schools_1')
    item_name = f"{selected_options} 參與靜宜大學申請入學主要原因(複選)"
    
    ##### 產出 result_df: 加條件: 挑選出 selected_options 中的特定高中
    if 系_院_校 == '0':
        # df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
        # df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
    if 系_院_校 == '1':
        # df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用
    if 系_院_校 == '2':
        # df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用

    

    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission_restrict, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 16, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=0, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission_restrict, df_admission_faculty=df_admission_faculty_restrict)    
    # Draw_2(column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 14,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name='', rank=True, rank_number=5, df_admission=df_admission, df_admission_restrict=df_admission_restrict)    
st.markdown("##")  ## 更大的间隔 



###### 認識與瞭解靜宜大學的管道(複選)
with st.expander("Q8. 認識與瞭解靜宜大學的管道(複選):"):
    # df_admission.iloc[:,7] ## 
    column_index = 7
    item_name = "認識與瞭解靜宜大學的管道(複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])

    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
 
    rank_number = 5   # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 16, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 特定高中認識與瞭解靜宜大學的管道(複選)
with st.expander("Q8-特定高中. 特定高中認識與瞭解靜宜大學的管道(複選):"):
    # df_admission.iloc[:,7] ## 
    column_index = 7
    # item_name = "特定高中認識與瞭解靜宜大學的管道(複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5
    highlight_schools = ['清水高中','龍津高中','中港高中','弘文高中','新民高中','僑泰高中','立人高中']
    selected_options = st.multiselect('選擇重點高中：', highlight_schools, default=['清水高中','龍津高中'],key='highlight_schools_2')
    item_name = f"{selected_options} 認識與瞭解靜宜大學的管道(複選)"

    ##### 產出 result_df: 加條件: 挑選出 selected_options 中的特定高中
    if 系_院_校 == '0':
        # df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
        # df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
    if 系_院_校 == '1':
        # df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用
    if 系_院_校 == '2':
        # df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        # df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].str.contains(selected_options, regex=True)]
        df_admission_restrict = df_admission[df_admission['請問您的高中學校全名 ?'].apply(lambda x: any(school in x for school in selected_options))]
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用
 


    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission_restrict, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 16, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission_restrict, df_admission_faculty=df_admission_faculty_restrict)    
    # Draw_2(column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 14,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name='', rank=True, rank_number=5, df_admission=df_admission, df_admission_restrict=df_admission_restrict)    
    
st.markdown("##")  ## 更大的间隔 



###### 一階篩選公告後是否有收到通過學系之聯絡
with st.expander("Q10. 一階篩選公告後是否有收到通過學系之聯絡:"):
    # df_admission.iloc[:,9] ## 
    column_index = 9
    item_name = "一階篩選公告後是否有收到通過學系之聯絡"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    # rank_number = 5

    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=22,xlabel_fontsize = 20,ylabel_fontsize = 20,legend_fontsize = 20,xticklabel_fontsize = 20, yticklabel_fontsize = 20, annotation_fontsize = 20, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 一階篩選通過學系之聯絡，是否提升參加第二階段甄試之動機
with st.expander("Q11. 一階篩選通過學系之聯絡，是否提升參加第二階段甄試之動機:"):
    # df_admission.iloc[:,10] ## 
    column_index = 10
    item_name = "一階篩選通過學系之聯絡，是否提升參加第二階段甄試之動機"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    # rank_number = 5

    ##### 產出 result_df: 加條件: Q10回答有 '有收到' 者, 才能進行此題Q11
    if 系_院_校 == '0':
        df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
    if 系_院_校 == '1':
        df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用
    if 系_院_校 == '2':
        df_admission_restrict = df_admission[df_admission['申請入學一階篩選公告後，您是否有收到通過學系之聯絡以及後續招生流程的說明 ?']=='有收到']
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用


    result_df = Frequency_Distribution(df_admission_restrict, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission_restrict, df_admission_faculty=df_admission_faculty_restrict)    
    
st.markdown("##")  ## 更大的间隔



# ###### 是否有參加4/20或4/27靜宜大學舉辦之甄試說明會
# with st.expander("Q12. 是否有參加4/20或4/27靜宜大學舉辦之甄試說明會:"):
#     # df_admission.iloc[:,11] ## 
#     column_index = 11
#     item_name = "是否有參加4/20或4/27靜宜大學舉辦之甄試說明會"
#     column_title.append(df_admission.columns[column_index][0:])
#     # set(df_admission_original['科系'])
#     rank_number = 5

#     ##### 產出 result_df: 
#     result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
#     # #### 選取前面 5 筆資料
#     # result_df = result_df.head(rank_number)
#     ##### 存到 list 'df_streamlit'
#     df_streamlit.append(result_df)  

#     ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
#     # st.write(choice)
#     st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
#     st.write(result_df.to_html(index=False), unsafe_allow_html=True)
#     st.markdown("##")  ## 更大的间隔

#     ##### 使用Streamlit畫單一圖 & 比較圖
#     #### 畫比較圖時, 比較單位之選擇:
#     if 院_系 == '0':
#         ## 使用multiselect组件让用户进行多重选择
#         # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
#         selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
#     if 院_系 == '1':
#         ## 使用multiselect组件让用户进行多重选择
#         # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
#         selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

#     # Draw(院_系, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
#     # Draw(院_系, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
#     Draw(院_系, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 14,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name=item_name, rank=False, rank_number=rank_number)    
    
# st.markdown("##")  ## 更大的间隔 



###### 是否有參加4/20或4/27靜宜大學舉辦之甄試說明會
with st.expander("Q12. 是否有參加4/20或4/27靜宜大學舉辦之甄試說明會:"):
    # df_admission.iloc[:,11] ## 
    column_index = 11
    item_name = "是否有參加4/20或4/27靜宜大學舉辦之甄試說明會"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df: 

    # st.write(set([i for i in df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']]))
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    
    ##Q11 有將 df_admission, df_admission_faculty 縮小範圍(加條件), 現在要恢復使用 df_admission_whole, df_admission_faculty_whole
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 參加甄試說明會對於瞭解以及選擇學系是否有幫助 
with st.expander("Q13. 參加甄試說明會對於瞭解以及選擇學系是否有幫助:"):
    # df_admission.iloc[:,12] ## 
    column_index = 12
    item_name = "參加甄試說明會對於瞭解以及選擇學系是否有幫助"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df: 加條件: Q12回答 '是' 者, 才能進行此題Q13
    if 系_院_校 == '0':
        df_admission_restrict = df_admission[df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']=='是']
        df_admission_faculty_restrict = df_admission_faculty[df_admission_faculty['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']=='是']
    if 系_院_校 == '1':
        df_admission_restrict = df_admission[df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']=='是']
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用
    if 系_院_校 == '2':
        df_admission_restrict = df_admission[df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']=='是']
        df_admission_faculty_restrict = df_admission_restrict  ## 沒有作用


    result_df = Frequency_Distribution(df_admission_restrict, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)

    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 18, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission_restrict, df_admission_faculty=df_admission_faculty_restrict)    
    
st.markdown("##")  ## 更大的间隔 



###### 對於書審資料的準備，你曾經由哪些管道獲得幫助與指引(複選)
with st.expander("Q16. 對於書審資料的準備，你曾經由哪些管道獲得幫助與指引(複選):"):
    # df_admission.iloc[:,15] ## 
    column_index = 15
    item_name = "對於書審資料的準備，你曾經由哪些管道獲得幫助與指引(複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df: 

    # st.write(set([i for i in df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']]))
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    ##Q13 有將 df_admission, df_admission_faculty 縮小範圍(加條件), 現在要恢復使用 df_admission_whole, df_admission_faculty_whole
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=18,xlabel_fontsize = 16,ylabel_fontsize = 16,legend_fontsize = 16,xticklabel_fontsize = 16, yticklabel_fontsize = 16, annotation_fontsize = 16, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 您曾經由哪些管道了解書審資料上傳到甄選會系統的操作步驟(複選)
with st.expander("Q18. 您曾經由哪些管道了解書審資料上傳到甄選會系統的操作步驟(複選):"):
    # df_admission.iloc[:,17] ## 
    column_index = 17
    item_name = "您曾經由哪些管道了解書審資料上傳到甄選會系統的操作步驟(複選)"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    # st.write(set([i for i in df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']]))
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=18,xlabel_fontsize = 16,ylabel_fontsize = 16,legend_fontsize = 16,xticklabel_fontsize = 16, yticklabel_fontsize = 16, annotation_fontsize = 16, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 政府對於私立大專校院每年減免學費3.5萬元之後，您知道靜宜大學每學期學費與其他國立大學差距僅約4000-6000元嗎 ?
with st.expander("Q20. 政府對於私立大專校院每年減免學費3.5萬元之後，您知道靜宜大學每學期學費與其他國立大學差距僅約4000-6000元嗎 ?"):
    # df_admission.iloc[:,19] ## 
    column_index = 19
    item_name = "政府對於私立大專校院每年減免學費3.5萬元之後，您知道靜宜大學每學期學費與其他國立大學差距僅約4000-6000元嗎 ?"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    # st.write(set([i for i in df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']]))
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 12,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 目前教育部的學費補助措施是否會增加您就讀靜宜大學的意願 ?
with st.expander("Q21. 目前教育部的學費補助措施是否會增加您就讀靜宜大學的意願 ?"):
    # df_admission.iloc[:,20] ## 
    column_index = 20
    item_name = "目前教育部的學費補助措施是否會增加您就讀靜宜大學的意願 ?"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    # st.write(set([i for i in df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']]))
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 10,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 您知道靜宜大學今年對於各入學管道提供最高達10萬元之獎學金及續領的訊息嗎 ?
with st.expander("Q22. 您知道靜宜大學今年對於各入學管道提供最高達10萬元之獎學金及續領的訊息嗎 ?"):
    # df_admission.iloc[:,21] ## 
    column_index = 21
    item_name = "您知道靜宜大學今年對於各入學管道提供最高達10萬元之獎學金及續領的訊息嗎 ?"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    # st.write(set([i for i in df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']]))
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=18,xlabel_fontsize = 16,ylabel_fontsize = 16,legend_fontsize = 16,xticklabel_fontsize = 16, yticklabel_fontsize = 16, annotation_fontsize = 16, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔



###### 靜宜大學今年對於各入學管道提供之獎學金訊息是否會增加您就讀靜宜大學的意願 ?
with st.expander("Q23. 靜宜大學今年對於各入學管道提供之獎學金訊息是否會增加您就讀靜宜大學的意願 ?"):
    # df_admission.iloc[:,22] ## 
    column_index = 22
    item_name = "靜宜大學今年對於各入學管道提供之獎學金訊息是否會增加您就讀靜宜大學的意願 ?"
    column_title.append(df_admission.columns[column_index][0:])
    # set(df_admission_original['科系'])
    rank_number = 5

    ##### 產出 result_df
    # st.write(set([i for i in df_admission['請問: 您是否有參加4/20或4/27靜宜大學舉辦之甄試說明會 ?']]))
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1)    
    # #### 選取前面 5 筆資料
    # result_df = result_df.head(rank_number)
    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    
    Draw(系_院_校, column_index, split_symbol='\n', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=15,xlabel_fontsize = 14,ylabel_fontsize = 14,legend_fontsize = 10,xticklabel_fontsize = 14, yticklabel_fontsize = 14, annotation_fontsize = 14, bar_width = 0.2, fontsize_adjust=0, item_name=item_name, rank=False, rank_number=rank_number, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



st.markdown("""
<style>
.bold-small-font {
    font-size:18px !important;
    font-weight:bold !important;
}
</style>
<p class="bold-small-font">第二階段甄試服務滿意度</p>
""", unsafe_allow_html=True)

###### 【考場指標】滿意度
with st.expander("Q24. 【考場指標】滿意度:"):
    # df_admission.iloc[:,23] ## 
    column_index = 23
    item_name = "【考場指標】滿意度"
    column_title.append(df_admission.columns[column_index][0:])


    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)

    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 16, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 【甄試流程】滿意度
with st.expander("Q26. 【甄試流程】滿意度:"):
    # df_admission.iloc[:,25] ## 
    column_index = 25
    item_name = "【甄試流程】滿意度"
    column_title.append(df_admission.columns[column_index][0:])


    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)

    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 16, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔 



###### 【接駁車服務】滿意度
with st.expander("Q28. 【接駁車服務】滿意度:"):
    # df_admission.iloc[:,27] ## 
    column_index = 27
    item_name = "【接駁車服務】滿意度"
    column_title.append(df_admission.columns[column_index][0:])


    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)

    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 16, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔



###### 【服務人員的交通引導(停車或考場位置引導)】滿意度
with st.expander("Q30. 【服務人員的交通引導(停車或考場位置引導)】滿意度:"):
    # df_admission.iloc[:,29] ## 
    column_index = 29
    item_name = "【服務人員的交通引導(停車或考場位置引導)】滿意度"
    column_title.append(df_admission.columns[column_index][0:])


    ##### 產出 result_df
    result_df = Frequency_Distribution(df_admission, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1)

    ##### 存到 list 'df_streamlit'
    df_streamlit.append(result_df)  

    ##### 使用Streamlit展示DataFrame "result_df"，但不显示索引
    # st.write(choice)
    st.write(f"<h6>{choice}</h6>", unsafe_allow_html=True)
    st.write(result_df.to_html(index=False), unsafe_allow_html=True)
    st.markdown("##")  ## 更大的间隔

    ##### 使用Streamlit畫單一圖 & 比較圖
    # #### 畫比較圖時, 比較單位之選擇:
    # if 系_院_校 == '0':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學系：', df_admission_original['科系'].unique(), default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    #     selected_options = st.multiselect('選擇比較學系：', departments_list, default=[choice,'企業管理學系'],key=str(column_index)+'d')  ## # selected_options = ['化科系','企管系']
    # if 系_院_校 == '1':
    #     ## 使用multiselect组件让用户进行多重选择
    #     # selected_options = st.multiselect('選擇比較學院：', df_admission_original['學院'].unique(), default=[choice,'資訊學院'],key=str(column_index)+'f')
    #     selected_options = st.multiselect('選擇比較學院：', faculties_list, default=[choice,'資訊學院'],key=str(column_index)+'f')

    # Draw(系_院_校, column_index, ';', '沒有工讀', 1, result_df, selected_options, dataframes, combined_df)
    # Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df, selected_options)
    Draw(系_院_校, column_index, split_symbol=';', dropped_string='沒有工讀', sum_choice=1, result_df=result_df, selected_options=selected_options, dataframes=dataframes, combined_df=combined_df, width1=10,heigh1=6,width2=11,heigh2=8,width3=10,heigh3=6,title_fontsize=20,xlabel_fontsize = 18,ylabel_fontsize = 18,legend_fontsize = 18,xticklabel_fontsize = 16, yticklabel_fontsize = 18, annotation_fontsize = 18, bar_width = 0.2, fontsize_adjust=1, item_name=item_name, rank=False, rank_number=5, df_admission=df_admission, df_admission_faculty=df_admission_faculty)    
    
st.markdown("##")  ## 更大的间隔  

 

