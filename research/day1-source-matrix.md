# ممیزی منبع فصل‌های روز نخست · ۱۱ مهر ۱۴۰۵

این پرونده ورودی نگارش است، نه جزوهٔ کامل. هر ردیف مرجع انگلیسی است و میزان بررسی واقعی را نشان می‌دهد. برای تبدیل هر فصل به `ready` باید **همهٔ بخش‌های مرتبط دست‌کم چهار منبع از چهار دانشگاه** خوانده، مقایسه و با ریزمبحث‌ها و سؤال‌های آزمون تطبیق داده شود. وجود چهار پیوند به‌تنهایی این شرط را برآورده نمی‌کند.

## منطق گزاره‌ها و گزاره‌نماها (`d_logic`)

مرزبندی: گزاره، ارزش، عملگرها، هم‌ارزی، گزاره‌نما، کمیت‌گذار. روش‌های عمومی اثبات در فصل `d_proof` و استقرا در فصل `d_induction` قرار دارند. پیش‌نویس فعلی در `study-planner/dist/chapters/d_logic.html` است.

| Course and exact material | Role and actual review | Remaining work |
|---|---|---|
| MIT — 6.042J Mathematics for Computer Science — Tom Leighton and Marten van Dijk — Chapter 1, Propositions — https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/7853d585044ef21bce5f48ce5fc89d28_MIT6_042JF10_chap01.pdf | Foundational definitions and truth-table reasoning; opening material initially reviewed. | Review the entire chapter segment relevant to this topic. |
| Stanford University — CS103 Mathematical Foundations of Computing — Luca Trevisan — Lecture 9, Mathematical Logic — https://cs.stanford.edu/people/trevisan/cs103-14/lecture09.pdf | Syntax, semantics, and quantified statements; propositional and some first-order content initially reviewed. | Complete the first-order portion and reconcile notation. |
| UC Berkeley — CS70 Discrete Mathematics and Probability Theory — Sanjit Seshia and Jean Walrand — Note 1, Propositional Logic — https://www-inst.cs.berkeley.edu/~cs70/fa16/static/notes/n1.pdf | Intuitive translation and truth tables; first two pages initially reviewed. | Review remaining pages and related exercises. |
| Carnegie Mellon University — 15-311 Logic and Mechanized Reasoning — Marijn Heule — Propositional Logic and First-Order Logic slides — https://www.cs.cmu.edu/~mheule/15311-s26/slides/prop.pdf | Formal syntax and semantics; introductory syntax slides initially reviewed. | Review all slides relevant to this chapter and compare scope. |

## نوع داده و تبدیل نوع (`p_types`)

مرزبندی: مقدار و نوع، متغیر و انتساب، عملگرها، تبدیل نوع، دامنهٔ نمایش و سرریز. ساختار کنترل برنامه در فصل `p_flow` و نمایش دودوییِ مفصل در فصل `g_number` است. تفاوت قواعد Python، C، Java و C0 باید **با نام زبان** ذکر شود؛ هیچ قاعدهٔ یک زبان نباید بی‌قید به زبان دیگر منتقل شود.

| Course and exact material | Role and actual review | Remaining work |
|---|---|---|
| MIT — 6.100L Introduction to CS and Programming Using Python — Ana Bell — Lecture 1, Introduction — https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_lec01.pdf | Expression values, object types, and name binding; relevant slides identified and initially inspected. | Read and compare every relevant slide, including numeric operations and conversion. |
| Stanford University — CS106A Programming Methodology — Eric Roberts — Expressions slides — https://cs.stanford.edu/people/eroberts/courses/cs106a/handouts/15-expression-slides.pdf | Variables, expressions, and static type viewpoint; source opened, content comparison pending. | Read all relevant slides and check Java-specific rules. |
| Carnegie Mellon University — 15-122 Principles of Imperative Computation — Frank Pfenning — Lecture 2, Ints — https://www.cs.cmu.edu/~rjsimmon/15122-m14/lec/02-ints.pdf | Fixed-width integers and modular arithmetic; pages 1–5 initially inspected. | Read the remaining relevant pages and distinguish C0 from C behavior. |
| Harvard University — CS50x 2026 — Lecture 1 Notes, C — https://cs50.harvard.edu/x/notes/1/ | C types, variables, and overflow examples; Types and Variables sections initially inspected. | Read all sections relevant to operators and conversions; verify examples independently. |

## مبنا و نمایش اعداد (`g_number`)

مرزبندی: نمایش مکانی در مبناهای دو، هشت، ده و شانزده؛ تبدیل مبنا؛ نمایش بدون علامت و مکمل دو؛ بازه، سرریز و تفکیک الگوی بیت از تفسیر عددی. جبر بولی و گیت‌ها فصل‌های `g_boolean` و `g_gates` هستند.

| Course and exact material | Role and actual review | Remaining work |
|---|---|---|
| MIT — 6.004 Computation Structures — Chris Terman — Unit 1.1, Annotated Slides — https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s1/ | Binary positional value, fixed-width unsigned range, and hexadecimal grouping; relevant text initially inspected. | Read the full unit segment and related worksheet. |
| Cornell University — CS3410 Computer System Organization — Numbers notes — https://courses.cs.cornell.edu/cs3410/2026sp/notes/numbers.html | Place value and conversion algorithms; initial sections inspected. | Review signed representation and worked examples completely. |
| University of Cambridge — Digital Electronics — Ian Wassell — Part I lecture notes — https://www.cl.cam.ac.uk/teaching/1011/DigElec/PartI.pdf | Binary numbers, signed representation, and logic-design context; relevant excerpt initially inspected. | Read and compare the entire number-representation portion. |
| Carnegie Mellon University — 15-122 Principles of Imperative Computation — Frank Pfenning — Lecture 2, Ints — https://www.cs.cmu.edu/~rjsimmon/15122-m14/lec/02-ints.pdf | Repeated division, modular arithmetic, two's complement; pages 1–5 initially inspected. | Complete the relevant pages and verify the range and overflow derivations. |

## بازبینی پیش از انتشار

- برای هر فصل، جدول ریزمبحث به صفحه یا بخش هر چهار منبع وصل شود و اختلاف تعریف‌ها و قراردادهای زبان/ماشین حل شود.
- سؤال‌های آزمون ایران فقط با شماره، صفحه و تصویر PDF اصلی وارد جزوه شوند. سؤال‌های دانشگاهی نیز با پیوند منبع و سطح ارتباط با آزمون مشخص شوند.
- دست‌کم پنج تا ده مسئلهٔ پیچیده با حل کامل و کنترل مستقل ارائه شود. صورت سؤال‌های دارای حق نشر تنها در حد مجاز با ارجاع یا بازنویسی مستقل استفاده شود.
- بخش‌های ناتمام و سطح واقعی بررسی منابع آشکار بمانند؛ این پرونده به معنی آمادگی هیچ‌کدام از سه جزوه نیست.
