# DFS Ad Compliance — Test Cases

Three test cases for evaluating the dfs-ad-compliance skill.
Expected verdicts are noted so you can judge skill accuracy.

---

## Test Case 1 — EXPECTED: NON-COMPLIANT (multiple hard fails)

**Format:** Facebook/Meta sponsored ad  
**Copy:**

> **Digital Finance Solutions — Australia's #1 Independent Mortgage Broker**
>
> We've helped 1,000+ Australians get guaranteed home loan approval — even with bad credit.
>
> ✅ 100% success rate
> ✅ No credit check required for pre-approval
> ✅ Access every lender in Australia
> ✅ Rates from 5.49% p.a.
>
> We work independently — no bias, no bank pressure. Just the best deal for YOU.
>
> 🔥 Get pre-approved in 24 hours — guaranteed.
>
> [Call us today] [Apply Now]

**What should be flagged:**
- "Independent" / "no bias" — prohibited terms (s160B)
- "guaranteed home loan approval" — misleading
- "100% success rate" — misleading (RG 234 Example 58)
- "No credit check required" — misleading
- "Access every lender in Australia" — misleading scope claim (RG 234 Example 64)
- "Rates from 5.49% p.a." — comparison rate missing (s160 National Credit Code)
- "pre-approved in 24 hours — guaranteed" — dual problem: false pre-approval claim + guarantee
- ACL number absent from paid ad

---

## Test Case 2 — EXPECTED: NEEDS FIXES (one borderline issue)

**Format:** Blog article introduction (editorial content, not paid ad)  
**Copy:**

> **How to Compare Home Loans and Actually Save Money**
>
> With interest rates shifting through 2025 and 2026, more Australians are looking to refinance or buy their first home. At Digital Finance Solutions, we work with a panel of Australia's leading lenders to help you find a loan that suits your situation.
>
> Refinancing at the right time can save you thousands over the life of your loan — but the right time depends on your individual circumstances, the fees involved, and your current rate compared to what's available in the market.
>
> In this article, we'll walk you through the key things to look at when comparing home loans, including interest rates, comparison rates, fees, and loan features.
>
> *General information only. This article does not constitute financial advice. Credit eligibility criteria apply. Digital Finance Solutions is a mortgage broking business.*

**What should be flagged:**
- "save you thousands" — benefit claim; is "depends on your circumstances" sufficient balance? Borderline — the article body qualifies it but the opening sentence is the flag point.
- ACL number absent — blog; note as best practice, not a hard flag.
- Otherwise well-structured: lender panel correctly qualified, no prohibited terms, no rate cited so no comparison rate issue, disclaimer present.

---

## Test Case 3 — EXPECTED: COMPLIANT

**Format:** Website service page (homepage "About Us" section)  
**Copy:**

> **Expert Home Loan Help, Tailored to You**
>
> At Digital Finance Solutions, we're mortgage brokers — not lenders. We compare home loans from our panel of lenders and help you find an option that fits your financial situation.
>
> We take time to understand your goals, your income, and your circumstances before recommending anything. Because every borrower is different.
>
> Whether you're buying your first home, refinancing, or investing in property — we'll help you understand your options.
>
> *Credit eligibility criteria apply. Digital Finance Solutions Pty Ltd | Australian Credit Licence [ACL number]. General information only — not financial advice. Your financial situation is unique; consider whether this product is right for you.*

**What should be noted (not flagged):**
- No rates cited — no comparison rate obligation triggered
- No prohibited terms
- Lender panel correctly framed as "our panel of lenders"
- Disclaimer present and reasonably prominent
- ACL number included (placeholder shown — confirm actual number)
- Benefits ("find an option that fits") are inherently qualified ("help you find" not "guarantee")
- Only note: ACL number placeholder should be filled in before publishing
