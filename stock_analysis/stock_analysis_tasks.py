from crewai import Task
from textwrap import dedent

class StockAnalysisTasks():
  def research(self, agent, company):
    return Task(description=dedent(f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to the stock and
        its industry.
        Pay special attention to any significant events, market
        sentiments, and analysts' opinions. Also include upcoming 
        events like earnings and others.
  
        Your final answer MUST be a report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the stock.
        Also make sure to return the stock ticker.
        
        {self.__tip_section()}
  
        Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
      """),
      agent=agent
    )
    
  def financial_analysis(self, agent): 
    return Task(description=dedent(f"""
       Conduct a Comprehensive Analysis of the Currency Pair's Market Performance

        To provide a thorough understanding of the currency pair's market performance, it is essential to conduct a thorough analysis of its market trends and performance. This involves examining key market metrics, such as:

      Pip Movement: A measure of the currency pair's price movement in pips, indicating its volatility and potential for profit.
      Volatility Index: A measure of the currency pair's price movement over a given period, indicating its level of volatility.
      Trend Analysis: An examination of the currency pair's price movement over time, identifying trends and patterns.
      Risk Management: An assessment of the potential risks and rewards associated with trading the currency pair.
        In addition to these market metrics, it is crucial to analyze the currency pair's performance in comparison to other currency pairs and overall market trends. This includes:

      Peer Comparison: A comparison of the currency pair's performance to that of other currency pairs, providing insight into its relative strength and competitiveness.
      Market Trends: An examination of the overall market trends, including economic indicators, interest rates, and market sentiment, to understand the currency pair's position within the broader market.
      Final Report: A Clear Assessment of the Currency Pair's Market Performance, Strengths, Weaknesses, and Competitor Comparison

      The final report will provide a comprehensive assessment of the currency pair's market performance, including:

      Market Summary: A summary of the currency pair's market performance, highlighting its strengths and weaknesses.
      Market Analysis: A detailed analysis of the currency pair's market metrics, including its pip movement, volatility index, trend analysis, and risk management.
      Competitor Comparison: A comparison of the currency pair's performance to that of other currency pairs, highlighting its relative strength and competitiveness.
      Market Analysis: An examination of the overall market trends, including economic indicators, interest rates, and market sentiment, to understand the currency pair's position within the broader market.
      Conclusion: A summary of the currency pair's market performance, highlighting its strengths, weaknesses, and potential for future growth.
      {self.__tip_section()}

        Make sure to use the most recent data possible.
      """),
      agent=agent
    )

  def filings_analysis(self, agent):
    return Task(description=dedent(f"""
        Analyze the latest 10-Q and 10-K filings from EDGAR for
        the stock in question. 
        Focus on key sections like Management's Discussion and
        Analysis, financial statements, insider trading activity, 
        and any disclosed risks.
        Extract relevant data and insights that could influence
        the stock's future performance.

        Your final answer must be an expanded report that now
        also highlights significant findings from these filings,
        including any red flags or positive indicators for
        your customer.
        {self.__tip_section()}        
      """),
      agent=agent
    )

  def recommend(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize the analyses provided by the
        Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation. 
        
        You MUST Consider all aspects, including financial
        health, market sentiment, and qualitative data from
        EDGAR filings.

        Make sure to include a section that shows insider 
        trading activity, and upcoming events like earnings.

        Your final answer MUST be a recommendation for your
        customer. It should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formatted for your customer.
        {self.__tip_section()}
      """),
      agent=agent
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"
