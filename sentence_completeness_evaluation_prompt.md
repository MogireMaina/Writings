# Sentence Completeness Evaluation Prompt

## Purpose
Evaluate whether a given sentence can stand alone as a complete, self-contained statement that would be clear and natural to a reader encountering it without any prior context.

## Instructions
When provided with a sentence, systematically evaluate it using the following methodology:

---

## EVALUATION FRAMEWORK

### STEP 1: PRONOUN REFERENCE CHECK
Examine all pronouns in the sentence for clear antecedents.

**Pronouns to check:**
- Personal: he, she, it, they, we, you, him, her, them, us
- Possessive: his, her, its, their, our, your, mine, theirs
- Reflexive: himself, herself, itself, themselves, ourselves
- Demonstrative used pronominally: this, that, these, those (when standing alone)

**Questions to ask:**
1. Does each pronoun refer to a noun within the same sentence?
2. If not, would a reader know WHO or WHAT the pronoun refers to without prior context?
3. Is the referent ambiguous even within the sentence?

**Mark as INCOMPLETE if:**
- Any pronoun lacks a clear antecedent within the sentence
- The referent must be supplied from external context

---

### STEP 2: DEMONSTRATIVE AND DEICTIC EXPRESSION CHECK
Identify pointing words that reference external information.

**Expressions to check:**
- Demonstrative determiners: this/that/these/those + noun (e.g., "this belief," "that theory")
- Demonstrative adverbs: here, there, now, then
- Determiners implying previous mention: such, said, aforementioned, former, latter

**Questions to ask:**
1. Does "this/that/these/those" point to something mentioned in the same sentence?
2. Does "here/there" refer to a location established in the sentence itself?
3. Does "such" indicate a type or category already defined in the sentence?

**Mark as INCOMPLETE if:**
- Demonstratives point backward to unstated referents
- Spatial/temporal deixis relies on external context
- "Such" refers to a category not established in the sentence

---

### STEP 3: IMPLICIT CONTRAST AND COMPARISON CHECK
Look for words indicating contrast or comparison with unstated alternatives.

**Markers to check:**
- Contrast: "however," "otherwise," "on the other hand," "by contrast," "conversely," "instead," "rather"
- Unexpressed negations: "far from," "not," "neither...nor" (when contrasting with unstated positive)
- Comparison: "more/less than," "similarly," "likewise," "in the same way"
- Alternatives: "the other," "another," "one...the other"

**Questions to ask:**
1. If the sentence says "otherwise" or "by contrast," is the contrasted idea present in the sentence?
2. If it says "far from X," is the implied "actually Y" clear without context?
3. If it mentions "one" or "the other," are both options identified in the sentence?

**Mark as INCOMPLETE if:**
- Contrast words reference unstated alternatives
- "Otherwise" requires knowledge of what would happen if conditions were different
- "One...the other" mentions options not both defined in the sentence

---

### STEP 4: ANAPHORIC EXPRESSION CHECK
Identify words that substitute for or refer back to previous content.

**Expressions to check:**
- Pro-forms: "do so," "do it," "one" (as substitute)
- Substitution phrases: "the former," "the latter," "the above," "the following"
- Abstract reference: "this situation," "that problem," "this contradiction," "such cases"
- Quantifiers with implicit domain: "both," "either," "neither," "all," "each"

**Questions to ask:**
1. Does "both" refer to two things explicitly mentioned in the sentence?
2. Does "this [abstract noun]" (e.g., "this problem") refer to something described in the sentence itself?
3. Are "the former" and "the latter" pointing to entities listed in the same sentence?

**Mark as INCOMPLETE if:**
- Abstract nouns with demonstratives refer to external situations/concepts
- "Both," "either," "neither" reference entities not in the sentence
- Substitution depends on previously mentioned content

---

### STEP 5: ELLIPSIS AND GAPPING CHECK
Check for missing elements that readers must supply from context.

**Types to check:**
- Verb ellipsis: "John went to the store, and Mary too [went to the store]"
- Noun ellipsis: "I read three books and she [read] four [books]"
- Clause ellipsis: Responses like "Because X" without the main clause
- Comparative deletion: "This is better [than X]" without stating X

**Questions to ask:**
1. Are any grammatically required elements missing?
2. Can the missing elements be recovered from within the sentence?
3. Would a reader need prior sentences to understand the complete meaning?

**Mark as INCOMPLETE if:**
- Essential elements are deleted and not recoverable from the sentence
- The sentence is a fragment requiring previous sentence structure to complete

---

### STEP 6: PRESUPPOSITION AND IMPLIED INFORMATION CHECK
Identify assumptions the sentence makes about shared knowledge.

**What to check:**
- Definite articles: "the X" (presupposes X was introduced)
- Factive verbs: "realize," "discover," "regret" (presuppose truth of complement)
- Change-of-state verbs: "stop," "continue," "still" (presuppose prior state)
- Specific names/terms without introduction: proper nouns used without context

**Questions to ask:**
1. Does "the X" assume we already know which X is being discussed?
2. If someone "continues" doing something, is what they're continuing stated in the sentence?
3. Are specific people/places/concepts named without introduction or explanation?

**Mark as INCOMPLETE if:**
- Definite descriptions lack antecedents
- Change-of-state expressions require knowledge of prior state
- Proper nouns appear without sufficient context (except universally known entities)

---

### STEP 7: DISCOURSE CONNECTIVES CHECK
Look for words that explicitly link to previous discourse.

**Connectives to check:**
- Sequential: "then," "next," "subsequently," "afterwards," "meanwhile"
- Causal: "therefore," "thus," "consequently," "as a result," "for this reason"
- Additive: "moreover," "furthermore," "additionally," "also," "besides"
- Concessive: "nevertheless," "nonetheless," "even so," "still," "yet"

**Questions to ask:**
1. Does "therefore" draw a conclusion from premises stated in the same sentence?
2. Does "then" refer to a time or sequence established in the sentence?
3. Does "also" add to a list that exists within the sentence?

**Mark as INCOMPLETE if:**
- Discourse connectives link to external propositions
- Causal connectives draw conclusions from unstated premises
- Sequential markers reference unstated temporal framework

---

### STEP 8: SEMANTIC COMPLETENESS CHECK
Assess whether the sentence expresses a complete, self-contained idea.

**Questions to ask:**
1. Does the sentence make a complete assertion, question, or command?
2. Would a reader understand the main point without additional information?
3. Does the sentence feel like a continuation of a thought rather than a new thought?
4. Are there any "dangling" references that create a sense of incompleteness?

**Mark as INCOMPLETE if:**
- The sentence feels like it's in the middle of an explanation
- The main point depends on understanding something not stated
- The sentence raises more questions than it answers about its own content

---

### STEP 9: SYNTACTIC INTEGRITY CHECK
Verify the sentence is grammatically complete and well-formed.

**What to check:**
- Subject and predicate are both present
- No obvious sentence fragments (except intentional stylistic ones)
- No corrupted text or merged sentences
- Punctuation is coherent

**Mark as INCOMPLETE if:**
- The sentence is a genuine fragment lacking required elements
- Text appears corrupted or incorrectly merged
- Grammatical structure is broken

---

## OUTPUT FORMAT

After completing all 9 steps, provide your evaluation in the following format:

```
SENTENCE: [Quote the sentence]

EVALUATION: [COMPLETE / INCOMPLETE]

ANALYSIS:
- Step 1 (Pronouns): [Finding]
- Step 2 (Demonstratives): [Finding]
- Step 3 (Contrasts): [Finding]
- Step 4 (Anaphora): [Finding]
- Step 5 (Ellipsis): [Finding]
- Step 6 (Presuppositions): [Finding]
- Step 7 (Connectives): [Finding]
- Step 8 (Semantic): [Finding]
- Step 9 (Syntactic): [Finding]

SPECIFIC ISSUES: [List each problematic element]

VERDICT: This sentence [CAN / CANNOT] stand alone because [brief explanation].

REVISION SUGGESTION (if incomplete): [How the sentence could be made complete]
```

---

## EVALUATION CRITERIA SUMMARY

**Mark COMPLETE if:**
- All references are internal to the sentence
- No critical information depends on external context
- The sentence expresses a self-contained idea
- A reader with no prior context would understand it clearly

**Mark INCOMPLETE if:**
- Any pronoun, demonstrative, or reference depends on external context
- Contrast or comparison words reference unstated alternatives
- Discourse connectives link to previous/following content
- The sentence presupposes information not provided
- The main idea cannot be grasped without additional context

---

## IMPORTANT DISTINCTIONS

**COMPLETE but context-enriched:**
Some sentences may be grammatically and referentially complete but are part of a larger argument. Mark these as COMPLETE if they can be understood in isolation, even if fuller context adds depth.

Example: "History makes it possible for us to feel the potential density and perimeter of our being."
- Complete: Yes (no unclear references)
- Part of larger argument: Yes (but still comprehensible alone)

**INCOMPLETE due to unclear reference:**
These sentences cannot be understood without knowing what previous referents are.

Example: "This belief can be traced back to Edmund Burke."
- Incomplete: Yes ("this belief" - which belief?)
- Requires: Previous sentence establishing the belief

---

## EDGE CASES

1. **Generic pronouns:** "One must be careful" - COMPLETE (generic, not referential)
2. **Universal references:** "The sun rises in the east" - COMPLETE (shared knowledge)
3. **Rhetorical questions:** May be complete even if part of dialogue
4. **Intentional fragments:** Literary style may use fragments purposefully
5. **Quotes within sentences:** Referenced speech may contain incomplete elements but the containing sentence may be complete

---

## PRACTICE APPLICATION

Use this prompt by:
1. Inputting a single sentence
2. Working through each step systematically
3. Documenting findings at each step
4. Reaching a final verdict with justification
5. Providing revision suggestions for incomplete sentences

The goal is consistent, methodical evaluation that can be applied to any sentence to determine its independence and completeness.
