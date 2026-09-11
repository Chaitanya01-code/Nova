from typing import Dict, Any, Optional

from app.core.context.context_builder import ContextBuilder, NovaContext
from app.core.reasoning.engine import ReasoningEngine
from app.core.planning.planner import Planner
from app.core.decision.policies import PolicyEngine
from app.core.decision.engine import DecisionEngine
from app.core.execution.executor import ExecutionExecutor
from app.core.evaluation.evaluator import Evaluator
from app.core.evaluation.verifier import Verifier


class NovaCore:
    """End-to-end orchestration pipeline for transcript understanding."""

    def __init__(self):
        self.context_builder = ContextBuilder()
        self.reasoning_engine = ReasoningEngine()
        self.planner = Planner()
        self.policy_engine = PolicyEngine()
        self.decision_engine = DecisionEngine()
        self.executor = ExecutionExecutor()
        self.evaluator = Evaluator()
        self.verifier = Verifier()

    def process(self, transcript: str, context: str = "") -> Dict[str, Any]:
        nova_context = self.context_builder.build(transcript, context)
        reasoning = self.reasoning_engine.analyze(nova_context.__dict__)
        plan = self.planner.create_plan(nova_context.__dict__)
        policy = self.policy_engine.decide(reasoning.__dict__, plan.__dict__)
        decision = self.decision_engine.choose(nova_context.__dict__, reasoning.__dict__, policy)

        action = {
            "type": nova_context.user_intent,
            "description": f"Execute request for {nova_context.target or 'general'}",
        }
        result = self.executor.execute(action)

        evaluation = self.evaluator.evaluate(result)
        verified = self.verifier.verify(result)

        return {
            "context": {
                "transcript": nova_context.transcript,
                "intent": nova_context.user_intent,
                "target": nova_context.target,
                "topics": nova_context.topics,
                "context": nova_context.context,
            },
            "reasoning": {
                "goal": reasoning.goal,
                "assumptions": reasoning.assumptions,
                "risks": reasoning.risks,
                "confidence": reasoning.confidence,
            },
            "plan": {
                "steps": [step.__dict__ for step in plan.steps],
            },
            "decision": {
                "action": decision.action,
                "reason": decision.reason,
                "approved": decision.approved,
            },
            "execution": result,
            "evaluation": {
                "passed": evaluation.passed,
                "score": evaluation.score,
                "feedback": evaluation.feedback,
                "verified": verified,
            },
            "return_context": {
                "status": "ok",
                "intent": nova_context.user_intent,
                "target": nova_context.target,
                "summary": reasoning.goal,
            },
        }
