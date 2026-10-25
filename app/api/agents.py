
from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from app.db.database import engine

router = APIRouter(prefix="/agents", tags=["Agents"])


@router.get("/")
def get_agents():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("""
                    SELECT id, name, model_name, system_prompt,
                           status, created_at
                    FROM agents
                    ORDER BY id
                """)
            )

            agents = [
                dict(row)
                for row in result.mappings().all()
            ]

            return {
                "total": len(agents),
                "agents": agents
            }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch agents: {str(e)}"
        )
