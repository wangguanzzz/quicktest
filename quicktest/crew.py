from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    CodeInterpreterTool
#     DirectoryReadTool,
#     FileReadTool,
#     SerperDevTool,
#     WebsiteSearchTool
)
# from quicktest.tools.custom_tool import MyCustomTool
# Uncomment the following line to use an example of a custom tool
from quicktest.tools.quaterly_report import QreportTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# Instantiate tools
# docs_tool = DirectoryReadTool(directory='./blog-posts')
# file_tool = FileReadTool()
# search_tool = SerperDevTool()
# web_rag_tool = WebsiteSearchTool()

@CrewBase
class QuicktestCrew():
    """Quicktest crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            # tools=[search_tool, web_rag_tool],
            tools=[QreportTool()],
            #tools=[SerperDevTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
            max_rpm=500,
            # allow_code_execution=True
        )


    @task
    def financial_analyze(self) -> Task:
        return Task(
            config=self.tasks_config['financial_analyze'],
            agent=self.financial_analyst()
        )
    


    @crew
    def crew(self) -> Crew:
        """Creates the Quicktest crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=3,
            #planning=True
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )