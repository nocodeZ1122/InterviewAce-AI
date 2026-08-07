def build_question_context(question):
    return f"""
Title:
{question.title}

Difficulty:
{question.difficulty}

Topic:
{question.topic}

Description:
{question.description}

Examples:
{question.examples}

Constraints:
{question.constraints}
"""