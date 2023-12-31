from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain_qianwen import ChatQwen_v1

# 百度百科复制的信息
information_ok = r"""
姚明（Yao Ming），男，汉族，无党派人士，1980年9月12日出生于上海市徐汇区，祖籍江苏省苏州市吴江区震泽镇，前中国职业篮球运动员，司职中锋，现任亚洲篮球联合会主席、中国篮球协会主席、中职联公司董事长兼总经理， [4] 改革先锋奖章获得者。
1998年4月，姚明入选王非执教的国家队，开始篮球生涯。2001年夺得CBA常规赛MVP，2002年夺得CBA总冠军以及总决赛MVP，分别3次当选CBA篮板王以及盖帽王，2次当选CBA扣篮王。2002年NBA选秀，他以状元秀身份被NBA的休斯敦火箭队选中，2003-09年连续6个赛季（生涯共8次）入选NBA全明星赛阵容，2次入选NBA最佳阵容二阵，3次入选NBA最佳阵容三阵。2009年，姚明收购上海男篮，成为上海久事大鲨鱼俱乐部老板。2011年7月20日，姚明宣布退役。
2015年2月10日，姚明正式成为北京申办冬季奥林匹克运动会形象大使之一。2016年4月4日，姚明正式入选2016年奈史密斯篮球名人纪念堂，成为首位获此殊荣的中国人；10月，姚明成为中国“火星大使”；11月，当选CBA公司副董事长。 [6]
2017年10月20日，姚明已将上海哔哩哔哩俱乐部全部股权转让。 [7] 2018年9月，荣获第十届“中华慈善奖”慈善楷模奖项。 [8] 2019年10月28日，胡润研究院发布《2019胡润80后白手起家富豪榜》，姚明以22亿元排名第48。
"""

if __name__ == "__main__":
    summary_template = """
        根据给定的个人信息 {information} 总结出以下内容:
        1. 简介
        2. 近期动态
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    chat_llm = ChatQwen_v1(
        model_name="qwen-turbo",
        temperature=0.5,
    )

    chain = LLMChain(
        llm=chat_llm,
        prompt=summary_prompt_template,
    )

    print(chain.predict(information=information_ok))
