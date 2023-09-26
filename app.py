import time
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Financial Data")
    st.text("这里将会为你展示苹果公司的5年内财务数据。")

    menu = ["概要","财务"]
    choice = st.sidebar.selectbox("目录",menu)
    if choice == "概要":
        overview_section()
    elif choice == "财务":
        financial_section()

def overview_section():
    st.header("概要")
    st.write("""
苹果公司(Apple Inc. )是美国高科技公司。它的产业包括设计、制造和销售消费电子、计算机软件和在线服务等。苹果的硬件产品包括iPhone、iPad、Mac、iPod、Apple Watch、Apple TV等。
""")

def financial_section():
    st.header("财务")
    financial_menu = ["财务指标", "利润表", "资产负债表", "现金流量表"]
    financial_choice = st.selectbox("目录", financial_menu)

    if financial_choice == "财务指标":
        financial_indicators_section()
    elif financial_choice == "利润表":
        income_statement_section()
    elif financial_choice == "资产负债表":
        balance_sheet_section()
    else :
        cash_flow_statement_section()

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False

def financial_indicators_section():
    st.subheader("财务指标")

    @st.cache_resource  
    def load_data():
        return pd.read_csv("F:/financial_data_AAPL_financialindicator.csv",encoding='utf-8')

    data = load_data()

    indicator_notes = {
        '股东权益比率':'''
        股东权益比率（又称自有资本比率或净资产比率）是股东权益与资产总额的比率，该比率反映企业资产中有多少是所有者投入的。股东权益比率应当适中。
        如果权益比率过小，表明企业过度负债，容易削弱公司抵御外部冲击的能力；而权益比率过大，意味着企业没有积极地利用财务杠杆作用来扩大经营规模。
        ''',

        '净利率': '''
        净利率是指公司净利润与销售收入的比值，通常以百分比表示。这个指标反映的是公司的盈利效率，或者说是公司每一元销售收入中实际获得的利润部分。
        净利率越高，表示公司的盈利效率越高，公司的盈利能力越强。
        ''',

        '毛利率':'''持续竞争优势往往会产生更高的毛利率 ％。因此公司可以按毛利率 ％分为以下几类：
        a. 毛利率 ％大于40％ --> 持续竞争优势
        b. 毛利率 ％介于20％和40％之间 --> 竞争优势下降
        c. 毛利率 ％低于20％ --> 不可持续的竞争优势
        毛利率 = 毛利/营业收入
        ''',

        '资产收益率': '''资产收益率（Return on Assets，简称ROA）也叫资产回报率，是用来衡量每单位资产创造多少净利润的指标，评估公司相对其总资产值的盈利能力的有用指标。
        对于零售业而言，资产收益率 ROA ％通常会高于5％。对于银行而言，资产收益率 ROA ％接近其利差。银行的资产收益率 ROA ％通常远低于2％。
        资产回报率 = 税后净利润 / 总资产
        ''',

        '流动比率':'''流动比率是衡量公司用短期资产偿还短期债务能力的指标。流动比率和速动比率越高，说明企业资产的变现能力越强，短期偿债能力亦越强。
        一般认为流动比率应在2:1以上.流动比率2:1，表示流动资产是流动负债的两倍，即使流动资产有一半在短期内不能变现，也能保证全部的流动负债得到偿还。
        流动比率 = 流动资产/流动负债
        ''',

        '速动比率':'''速动比率是衡量公司用高流动性的短期资产偿还短期债务能力的指标。流动比率和速动比率越高，说明企业资产的变现能力越强，短期偿债能力亦越强。
        一般认为速动比率应在1:1以上。速动比率 1:1，表示现金等具有即时变现能力的速动资产与流动负债相等，可以随时偿付全部流动负债。
        速动比率 = 速动资产/流动负债\n速动资产 = 流动资产 - 预付账款 - 存货
        ''',

        '资产周转率': '''资产周转率是衡量企业资产管理效率的重要财务比率，体现了企业经营期间全部资产从投入到产出的流转速度。
        资产周转率 = 总营业收入/总资产
        ''',

        '存货周转率': '''存货周转率可以衡量公司一年内库存周转的速度。较高的存货周转率意味着该公司库存较少。
        因此，公司在存储，减记和过时的库存上花费的钱更少。但如果库存太少，则可能会影响销售，因为公司可能不足以满足需求。
        ''',

        '净资产收益率': '''净资产收益率(Return on Equity，简称 ROE)是指公司净利润与公司净资产的比值，也通常以百分比表示。
        这个指标反映的是公司资本的盈利能力，或者说是公司每一元净资产在一定期间内可以创造的利润。
        ROE越高，表示公司的资本盈利能力越强，对投资者的吸引力也就越大。
        在15％到20％之间的股本回报率 ROE ％被认为是可取的。
        计算公式为：净资产收益率 = 净利润 / 平均净资产
        ''',
    }

    indicators = data['Unnamed: 0'].tolist()

    selected_indicator = st.selectbox("注释", indicators)

    note = indicator_notes.get(selected_indicator, '')
    if note:
        st.write(note)

    def plot_indicator(indicator_data):

        years = [str(year) for year in range(2018, 2023)]
        amounts = indicator_data[1:11:2].values

        yoy_values = [float(str(val).replace('%', '')) for val in indicator_data[2:12:2]]

        fig, ax1 = plt.subplots(figsize=(10, 6))

        bars = ax1.bar(years, amounts, color='palegreen', alpha=0.6, label='金额')
        ax1.set_xlabel('年份')
        ax1.set_ylabel('金额', color='forestgreen')
        ax1.tick_params(axis='y', labelcolor='forestgreen')

        ax2 = ax1.twinx()
        ax2.plot(years, yoy_values, color='red', marker='o', label='YoY增长率')
        ax2.set_ylabel('YoY增长率(%)', color='red')
        ax2.tick_params(axis='y', labelcolor='red')

        ax1.set_title(indicator_data['Unnamed: 0'])

        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        for bar in bars:
            yval = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', color='black')

        plt.tight_layout()
        plt.show()

        st.pyplot(fig)
        st.subheader("")

    for index, row in data.iterrows():
        plot_indicator(row)
    
    row = data[data['Unnamed: 0'] == selected_indicator].iloc[0]
    plot_indicator(row)
    

def income_statement_section():
    st.subheader("利润表")
    st.text('Income Statement: 提供了公司一段时间内（如一季度或一年）的收入和费用信息，以及净利润。')

    @st.cache_resource  
    def load_data():
        return pd.read_csv("F:/financial_data_AAPL_income.csv",encoding='utf-8')

    data = load_data()

    def plot_indicator(indicator_data):

        years = [str(year) for year in range(2018, 2023)]
        amounts = indicator_data[1:11:2].values

        yoy_values = [float(str(val).replace('%', '')) for val in indicator_data[2:12:2]]

        fig, ax3 = plt.subplots(figsize=(10, 6))
    
        bars = ax3.bar(years, amounts, color='palegreen', alpha=0.6, label='金额')
        ax3.set_xlabel('年份')
        ax3.set_ylabel('金额', color='forestgreen')
        ax3.tick_params(axis='y', labelcolor='forestgreen')

        ax4 = ax3.twinx()
        ax4.plot(years, yoy_values, color='red', marker='o', label='YoY增长率')
        ax4.set_ylabel('YoY增长率(%)', color='red')
        ax4.tick_params(axis='y', labelcolor='red')

        ax3.set_title(indicator_data['Unnamed: 0'])

        ax3.legend(loc='upper left')
        ax4.legend(loc='upper right')

        for bar in bars:
            yval = bar.get_height()
        if isinstance(yval, (int, float)):
            ax3.text(bar.get_x() + bar.get_width()/2, yval, str(round(yval, 2)), ha='center', va='bottom', color='black')
        else:
            pass
        plt.tight_layout()
        plt.show()

        st.pyplot(fig)

    for index, row in data.iterrows():
        plot_indicator(row)

def balance_sheet_section():
    st.subheader("资产负债表")
    st.text('Balance Sheet: 描述了公司的资产、负债和股东权益。')

    @st.cache_resource  
    def load_data():
        return pd.read_csv("F:/financial_data_AAPL_balance.csv",encoding='utf-8')

    data = load_data()

    def plot_indicator(indicator_data):

        years = [str(year) for year in range(2018, 2023)]
        amounts = indicator_data[1:11:2].values

        yoy_values = [float(str(val).replace('%', '')) for val in indicator_data[2:12:2]]

        fig, ax5 = plt.subplots(figsize=(10, 6))

        bars = ax5.bar(years, amounts, color='palegreen', alpha=0.6, label='金额')
        ax5.set_xlabel('年份')
        ax5.set_ylabel('金额', color='forestgreen')
        ax5.tick_params(axis='y', labelcolor='forestgreen')

        ax6 = ax5.twinx()
        ax6.plot(years, yoy_values, color='red', marker='o', label='YoY增长率')
        ax6.set_ylabel('YoY增长率(%)', color='red')
        ax6.tick_params(axis='y', labelcolor='red')

        ax5.set_title(indicator_data['Unnamed: 0'])

        ax5.legend(loc='upper left')
        ax6.legend(loc='upper right')

        for bar in bars:
            yval = bar.get_height()
            ax5.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', color='black')

        plt.tight_layout()
        plt.show()

        st.pyplot(fig)

    for index, row in data.iterrows():
        plot_indicator(row)


def cash_flow_statement_section():
    st.subheader("现金流量表")
    st.text('Cash Flow Statement: 揭示了公司在操作、投资和融资活动中现金的流入和流出。')

    @st.cache_resource  
    def load_data():
        return pd.read_csv("F:/financial_data_AAPL_cash.csv",encoding='utf-8')

    data = load_data()

    def plot_indicator(indicator_data):

        years = [str(year) for year in range(2018, 2023)]
        amounts = indicator_data[1:11:2].values

        yoy_values = [float(str(val).replace('%', '')) for val in indicator_data[2:12:2]]

        fig, ax7 = plt.subplots(figsize=(10, 6))

        bars = ax7.bar(years, amounts, color='palegreen', alpha=0.6, label='金额')
        ax7.set_xlabel('年份')
        ax7.set_ylabel('金额', color='forestgreen')
        ax7.tick_params(axis='y', labelcolor='forestgreen')

        ax8 = ax7.twinx()
        ax8.plot(years, yoy_values, color='red', marker='o', label='YoY增长率')
        ax8.set_ylabel('YoY增长率(%)', color='red')
        ax8.tick_params(axis='y', labelcolor='red')

        ax7.set_title(indicator_data['Unnamed: 0'])

        ax7.legend(loc='upper left')
        ax8.legend(loc='upper right')

        for bar in bars:
            yval = bar.get_height()
            ax7.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', color='black')

        plt.tight_layout()
        plt.show()

        st.pyplot(fig)

    for index, row in data.iterrows():
        plot_indicator(row)

if __name__ == "__main__":
    main()