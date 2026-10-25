from pydantic import BaseModel, Field


class AgentConfigCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    model_name: str = Field(min_length=1, max_length=100)
    system_prompt: str = Field(min_length=1)


class AgentConfigResponse(AgentConfigCreate):
    id: str
    status: str = "created"