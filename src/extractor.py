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
    entity_type: EntityType = Field(
        ...,
        description = "The strict ontological category of the entity"
    )
    aliases: List[str] = Field(
        default_factory = list,
        description="Alternative names or aliass identified in the text"
    )
    
    @model_validator(mode = 'after')
    def normalize_name(self) -> 'CyberEntity':
        """ENsures consistent formatting for graph node keys by stripping whitespaces"""
        self.name = self.name.strip()
        return self