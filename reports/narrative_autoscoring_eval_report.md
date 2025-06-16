

This report summarizes the evaluation results for the narrative autoscoring system across five rubric categories.

## Rubric Scoring Agreement (Human vs LLM)

| Criteria                                  | Agreement Score |
|-------------------------------------------|-----------------|
| Setting, POV, Characters                  | 0.814           |
| Narrative Techniques                      | 0.876           |
| Theme/Message                             | 0.857           |
| Coherence (Organization)                  | 0.832           |
| Audience Appeal                           | 0.621           |

## Overrating / Underrating / Matching (Count)

| Criteria                  | Under | Over | Match |
|---------------------------|-------|------|-------|
| Setting, POV, Characters  | 12    | 64   | 322   |
| Narrative Techniques      | 21    | 21   | 356   |
| Theme/Message             | 14    | 36   | 348   |
| Coherence                 | 31    | 26   | 341   |
| Audience Appeal           | 175   | 6    | 217   |

## Key Problems Identified

### 1. Setting, Point of View, and Characters
- **Missed or weak settings scored too high**
  - _“The student introduces characters, but not the setting.”_
- **Narrator shifts not caught**
  - _“Who is telling the story? It switches and feels confusing.”_

### 2. Narrative Techniques
- **No dialogue or description, but LLM missed it**
  - _“Dialogue and vivid descriptions are missing but feedback doesn’t highlight this.”_

### 3. Theme or Message
- **LLM credited vague or missing themes**
  - _“The student hasn’t developed any message.”_
- **Did not help refine unclear ideas**
  - _“The message seems implied but not clearly stated.”_

### 4. Coherence
- **Missing conclusions not flagged**
  - _“The conclusion is really lacking.”_
- **Didn’t comment on missing transitions**
  - _“Transitions would improve the flow.”_

### 5. Audience Appeal
- **Didn’t mention lack of engagement or voice**
  - _“There isn't a lot to draw the reader in.”_
- **Tended to underrate otherwise readable writing**
  - _“Voice is consistent and clear — I’d give a 4.”_

## Fixes Implemented
We updated the prompt to:
- Recognize vague or missing themes more conservatively.
- Penalize missing narrative elements like dialogue and reflection.
- Be more generous with Audience Appeal where readability is good (Grades 3–5).
- Highlight structural issues (missing conclusions or transitions).
