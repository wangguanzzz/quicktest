from crewai_tools import BaseTool
import yfinance as yf
import pandas as pd

# 设置 pandas 显示选项
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_colwidth', None)  # 显示所有列宽
pd.set_option('display.max_seq_item', None)  # 显示所有序列项

class QreportTool(BaseTool):
    name: str = "QreportTool"
    description: str = (
        "Input the stock ticker, this tool will return the recent quaterly financial reports"
    )

    def get_quarterly_report(self,ticker):
        # 创建 Ticker 对象
        stock = yf.Ticker(ticker)
        
        # 获取季度财务报表数据
        quarterly_income_statement = stock.quarterly_financials
        quarterly_balance_sheet = stock.quarterly_balance_sheet
        quarterly_cash_flow = stock.quarterly_cashflow
        
        return quarterly_income_statement, quarterly_balance_sheet, quarterly_cash_flow


    def _run(self, argument: str) -> str:
        quarterly_income_statement, quarterly_balance_sheet, quarterly_cash_flow = self.get_quarterly_report(argument)
        
        return f"""
        quarterly_income_statement:
        {quarterly_income_statement}
        
        quarterly_balance_sheet:
        {quarterly_balance_sheet}
        
        quarterly_cash_flow:
        {quarterly_cash_flow}
        """
