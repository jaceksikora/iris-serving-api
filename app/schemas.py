from pydantic import BaseModel, Field

class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, description="The length of the petal.")
    sepal_width: float = Field(..., gt=0, description="The width of the petal.")
    petal_length: float = Field(..., gt=0, description="The length of the petal.")
    petal_width: float = Field(..., gt=0, description="The width of the petal.")