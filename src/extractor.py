from typing import List, Literal
from pydantic import BaseModel, Field, model_validator

#Strict categorial boundaries for security entities to prevent LLMs form inventing random category names
EntityType = Literal[
    "ThreatActor",
    "Malware",
    "Vulnerability",
    "Technique",
    "AssetTarget",
    "Indicator"
]

class CyberEntity(BaseModel):
    '''
    Represents a unique, cannonicalized entity node within the cybersecurity knowledge graph.
    '''
    name: str = Field(
        ...,
        description = "The normalized cannonical name of the entity"
    )