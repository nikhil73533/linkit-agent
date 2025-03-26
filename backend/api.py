from livekit.agents import llm
import enum
from typing import Annotated
import logging

logger = logging.getLogger("user-data")
logger.setLevel(logging.INFO)

class PersonalQueries(enum.Enum):
    LifeStory = "life_story"
    Superpower = "superpower"
    GrowthAreas = "growth_areas"
    Misconceptions = "misconceptions"
    PushingLimits = "pushing_limits"

class AssistantFnc(llm.FunctionContext):
    def __init__(self):
        super().__init__()
        
        self._personal_info = {
            PersonalQueries.LifeStory: "Hi, I am Nikhil Gupta, working at Celebal Technologies as a Software Engineer. I have a passion and deep interest in coding, which has led me to work on projects involving AI agents, RAG, and traditional software engineering techniques. I graduated from JK Lakshmipat University in Jaipur, which is also my hometown.",
            PersonalQueries.Superpower: "I never let things go easily. I put my whole effort into the work I do, and even if things go wrong, I never give up. I keep pushing myself to the edge of my comfort zone. If I ever feel frustrated, I take a break and start again with renewed energy.",
            PersonalQueries.GrowthAreas: "The top 3 areas I'd like to grow in are: 1) Improving my communication skills, as I am still a bit introverted, which limits my reach to people. 2) Enhancing my attention to detail—I quickly figure out the overall plan but sometimes miss common small details. 3) Multitasking—sometimes, I focus too much on a single task, causing other smaller tasks to get delayed.",
            PersonalQueries.Misconceptions: "A common misconception my coworkers have about me is that I am a very serious person. But inside, I truly enjoy my work and find joy in what I do.",
            PersonalQueries.PushingLimits: "I believe pushing boundaries is not hard if you have the courage to face situations outside your comfort zone. In every project, I challenge myself and learn something new, which helps me understand myself better. My never-give-up attitude keeps me motivated to keep pushing forward."
        }
    
    @llm.ai_callable(description="Get information about Nikhil Gupta's life story")
    def get_life_story(self):
        logger.info("Fetching life story")
        return self._personal_info[PersonalQueries.LifeStory]
    
    @llm.ai_callable(description="Get Nikhil Gupta's superpower")
    def get_superpower(self):
        logger.info("Fetching superpower")
        return self._personal_info[PersonalQueries.Superpower]
    
    @llm.ai_callable(description="Get the top 3 areas of growth for Nikhil Gupta")
    def get_growth_areas(self):
        logger.info("Fetching growth areas")
        return self._personal_info[PersonalQueries.GrowthAreas]
    
    @llm.ai_callable(description="Get common misconceptions about Nikhil Gupta")
    def get_misconceptions(self):
        logger.info("Fetching misconceptions")
        return self._personal_info[PersonalQueries.Misconceptions]
    
    @llm.ai_callable(description="Get how Nikhil Gupta pushes his boundaries and limits")
    def get_pushing_limits(self):
        logger.info("Fetching pushing limits")
        return self._personal_info[PersonalQueries.PushingLimits]
