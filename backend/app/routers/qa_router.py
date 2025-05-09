from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ..services.e_qa_system import answer_question
from ..auth.auth_handler import get_current_user

router = APIRouter(
    prefix="/qa",
    tags=["qa"]
)

class QuestionRequest(BaseModel):
    question: str
    document_ids: Optional[List[str]] = None

class QuestionResponse(BaseModel):
    answer: str
    sources: dict

@router.post("", response_model=QuestionResponse)
async def ask_document_question(
    request: QuestionRequest,
    user=Depends(get_current_user)
):
    """
    Answer a question about specific documents
    """
    result = await answer_question(
        query=request.question,
        user_id=user['id'],
        document_ids=request.document_ids
    )
    return result
