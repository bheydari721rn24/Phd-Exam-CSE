"""Readable source for the priority-one calendar; writes dist/schedule.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
subjects = {
    "discrete": {"title": "ریاضیات گسسته"},
    "programming": {"title": "مبانی برنامه‌سازی"},
    "algorithms": {"title": "داده‌ساختارها و الگوریتم‌ها"},
    "probability": {"title": "آمار و احتمال مهندسی"},
    "linear": {"title": "جبر خطی"},
    "logic": {"title": "مدار منطقی"},
    "ai": {"title": "هوش مصنوعی"},
}

topic_groups = {
    "discrete": {
        "d_logic": "منطق گزاره‌ها، گزاره‌نماها و هم‌ارزی‌ها",
        "d_sets": "مجموعه‌ها و عمل‌های مجموعه‌ای",
        "d_proof": "اثبات مستقیم، خلف و مثال نقض",
        "d_induction": "استقرای معمولی و قوی",
        "d_relations": "رابطه‌ها، هم‌ارزی و ترتیب جزئی",
        "d_functions": "تابع‌ها، وارون، تزریق و پوشا بودن",
        "d_invariants": "ناورداها و استدلال بازگشتی",
        "d_number": "تقسیم‌پذیری، پیمانه و مبانی نظریهٔ اعداد",
        "d_counting": "جایگشت، ترکیب و شمارش حالت‌ها",
        "d_inclusion": "شمول و عدم شمول",
        "d_pigeonhole": "اصل لانه‌کبوتری و کاربردها",
        "d_recurrence": "روابط بازگشتی و حل مقدماتی آن‌ها",
        "d_generating": "توابع مولد و روش‌های شمارش پیشرفته",
        "d_graph": "گراف، مسیر، همبندی و درجه",
        "d_trees": "درخت، پوشا و خواص ساختاری",
        "d_dprob": "احتمال گسسته و پیوند آن با شمارش",
    },
    "programming": {
        "p_rep": "نمایش عدد، نویسه و داده در رایانه",
        "p_types": "نوع داده، تبدیل نوع و عملگرها",
        "p_flow": "شرط، حلقه و ترتیب اجرای دستورها",
        "p_functions": "تابع، دامنهٔ متغیر و انتقال پارامتر",
        "p_arrays": "آرایه و اندیس‌گذاری",
        "p_strings": "رشته و پایان‌دهندهٔ آن",
        "p_recursion": "تابع بازگشتی و پشتهٔ فراخوانی",
        "p_pointers": "اشاره‌گر، هم‌نامی و حساب آدرس",
        "p_memory": "حافظهٔ پویا و طول عمر داده",
        "p_structs": "ساختار، رکورد و چیدمان داده",
        "p_bitwise": "عملگرهای بیتی و ماسک‌ها",
        "p_trace": "ردگیری کد، خطاهای مرزی و رفتار تعریف‌نشده",
    },
    "algorithms": {
        "a_model": "مدل محاسبه و تعریف اندازهٔ ورودی",
        "a_asym": "نمادگذاری مجانبی و مقایسهٔ رشد",
        "a_loop": "تحلیل حلقه‌ها و شمارش عملیات",
        "a_recurrence": "روابط بازگشتی و قضیه‌های حل آن‌ها",
        "a_divide": "تقسیم و حل و تحلیل آن",
        "a_arrays": "آرایه، فهرست پیوندی و هزینهٔ عملیات",
        "a_stackqueue": "پشته، صف و کاربردها",
        "a_sort": "مرتب‌سازی‌های مقایسه‌ای و غیرمقایسه‌ای",
        "a_select": "جست‌وجو، انتخاب و آمارهٔ ترتیبی",
        "a_bst": "درخت جست‌وجوی دودویی و پیمایش",
        "a_balanced": "درخت‌های متوازن و تحلیل ارتفاع",
        "a_heap": "هیپ و صف اولویت",
        "a_hash": "جدول هش، برخورد و تحلیل امیدی",
        "a_amortized": "تحلیل سرشکن و تغییر اندازهٔ پویا",
        "a_graphrep": "نمایش گراف و هزینهٔ پیمایش",
        "a_bfsdfs": "جست‌وجوی عرضی و عمقی",
        "a_topological": "ترتیب توپولوژیک و مؤلفه‌ها",
        "a_mst": "درخت پوشای کمینه",
        "a_shortest": "کوتاه‌ترین مسیر و شرط‌های الگوریتم‌ها",
        "a_greedy": "طراحی حریصانه و اثبات درستی",
        "a_dp": "برنامه‌ریزی پویا و طراحی حالت",
        "a_flow": "جریان شبکه و برش کمینه",
        "a_lower": "کران پایین و مسئله‌های سخت",
        "a_random": "الگوریتم تصادفی و تحلیل امیدی",
        "a_string": "الگوریتم‌های پایهٔ تطبیق رشته",
        "a_correct": "ناوردا، گواه درستی و مقایسهٔ روش‌ها",
    },
    "probability": {
        "s_axioms": "فضای نمونه، پیشامد و اصول احتمال",
        "s_counting": "شمارش احتمالاتی و استقلال",
        "s_conditional": "احتمال شرطی و قانون احتمال کل",
        "s_bayes": "قاعدهٔ بیز و نرخ پایه",
        "s_descriptive": "خلاصه‌سازی داده و آمار توصیفی",
        "s_discrete": "متغیر تصادفی گسسته و توزیع‌های رایج",
        "s_expectation": "امید ریاضی و خطی بودن آن",
        "s_variance": "واریانس، کوواریانس و همبستگی",
        "s_distributions": "دوجمله‌ای، هندسی، پواسون و تقریب‌ها",
        "s_continuous": "متغیر پیوسته، چگالی و توزیع‌های رایج",
        "s_joint": "توزیع مشترک و حاشیه‌ای",
        "s_condexp": "امید شرطی و استقلال متغیرها",
        "s_transform": "تبدیل متغیر و توزیع تابعی از متغیرها",
        "s_llnclt": "قانون اعداد بزرگ و قضیهٔ حد مرکزی",
        "s_sampling": "نمونه‌گیری و توزیع آماره‌ها",
        "s_estimation": "برآورد نقطه‌ای و فاصلهٔ اطمینان",
        "s_hypothesis": "آزمون فرض، خطاها و مقدار احتمال",
        "s_regression": "رگرسیون و همبستگی پایه",
        "s_markov": "زنجیرهٔ مارکوف مقدماتی",
    },
    "linear": {
        "l_vectors": "بردار، ضرب داخلی و هندسهٔ خطی",
        "l_matrices": "ماتریس و اعمال ماتریسی",
        "l_gauss": "حذف گاوسی و حل دستگاه خطی",
        "l_rank": "رتبه، وارون‌پذیری و دستگاه‌ها",
        "l_det": "دترمینان و خواص آن",
        "l_spaces": "فضا، زیرفضا، پایه و بعد",
        "l_linear": "تبدیل خطی، هسته و تصویر",
        "l_orthogonality": "عمودبودن و تجزیهٔ متعامد",
        "l_projection": "تصویر عمودی و ماتریس تصویر",
        "l_leastsquares": "کمترین مربعات و کاربردها",
        "l_eigen": "مقدار و بردار ویژه",
        "l_diagonal": "قطری‌سازی و ماتریس‌های متقارن",
        "l_svd": "تجزیهٔ مقادیر منفرد در حد پیوند با مباحث پایه",
    },
    "logic": {
        "g_number": "مبنای اعداد و کدگذاری دودویی",
        "g_boolean": "جبر بولی و جدول درستی",
        "g_gates": "گیت‌ها و پیاده‌سازی تابع",
        "g_kmap": "مین‌ترم، ماکس‌ترم و ساده‌سازی",
        "g_combin": "طراحی مدارهای ترکیبی",
        "g_arithmetic": "جمع‌کننده، مقایسه‌گر و مدار حسابی",
        "g_mux": "مالتی‌پلکسر، رمزگذار و دیکدر",
        "g_latch": "لچ و مبانی مدار ترتیبی",
        "g_ff": "فلیپ‌فلاپ و جدول تحریک",
        "g_register": "ثبات و انتقال داده",
        "g_counter": "شمارنده و دنبالهٔ حالت",
        "g_fsm": "ماشین حالت و طراحی آن",
        "g_timing": "زمان‌بندی، تأخیر و مسیر بحرانی",
        "g_hazards": "مخاطرهٔ منطقی و رفتار گذرا",
        "g_memory": "حافظه و منطق برنامه‌پذیر در حد مدار منطقی",
    },
    "ai": {
        "i_agents": "عامل، محیط و تعریف مسئله",
        "i_uninformed": "جست‌وجوی ناآگاهانه و سنجه‌های آن",
        "i_informed": "جست‌وجوی آگاهانه و تابع تخمین",
        "i_optimality": "کامل‌بودن، بهینگی و سازگاری تخمین",
        "i_games": "جست‌وجوی خصمانه و هرس",
        "i_csp": "مسئلهٔ ارضای قید و انتشار محدودیت",
        "i_prop": "بازنمایی دانش با منطق گزاره‌ای",
        "i_fol": "منطق محمولات و یکسان‌سازی",
        "i_inference": "استنتاج و راهبرد اثبات",
        "i_planning": "برنامه‌ریزی کلاسیک و فضای حالت",
        "i_bayes": "استنتاج احتمالاتی و قانون بیز",
        "i_bn": "شبکهٔ بیزی و استقلال شرطی",
        "i_decision": "تصمیم‌گیری تحت عدم‌قطعیت",
        "i_learning": "چارچوب یادگیری نظارت‌شده و تعمیم",
        "i_classification": "دسته‌بندی و ارزیابی مدل",
        "i_clustering": "خوشه‌بندی در حد مبانی هوش مصنوعی",
        "i_neural": "شبکهٔ عصبی در حد مبانی هوش مصنوعی",
        "i_eval": "بیش‌برازش، سنجه‌ها و خطاهای ارزیابی",
    },
}
topics = {topic_id: {"title": title, "subject": subject}
          for subject, entries in topic_groups.items()
          for topic_id, title in entries.items()}

def unit(subject, hours, title, ids, outcome):
    return {"subject": subject, "hours": hours, "title": title,
            "topicIds": ids.split(), "outcome": outcome}

def week(number, date_label, short_label, focus, units):
    return {"number": number, "phase": "اولویت اول · دور نخست",
            "dateLabel": date_label, "shortLabel": short_label, "focus": focus,
            "totalHours": sum(u["hours"] for u in units),
            "notice": "در دور نخست از شما تست گرفته نمی‌شود. پرسش‌های جزوه با حل کامل برای یادگیری ارائه می‌شوند.",
            "units": units}

weeks = [
    week(1, "۲ تا ۸ مهر", "پایهٔ مشترک", "تعریف، اثبات، مدل هزینه و زبان احتمال را می‌سازیم.", [
        unit("discrete", 14, "منطق و اثبات", "d_logic d_sets d_proof d_induction", "قضیه و برهان از مثال جدا شوند."),
        unit("algorithms", 16, "تحلیل اولیه", "a_model a_asym a_loop", "هزینهٔ حلقه را از شمارش عملیات استخراج کنید."),
        unit("probability", 12, "فضای نمونه و شمارش", "s_axioms s_counting", "فضای نمونه و استقلال را خلط نکنید."),
        unit("linear", 10, "بردار و ماتریس", "l_vectors l_matrices", "ضرب ماتریسی را با تفسیر هندسی بخوانید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن و واژه در بافت؛ بدون آزمون."),
    ]),
    week(2, "۹ تا ۱۵ مهر", "بازگشت و شرط", "از استدلال بازگشتی تا احتمال شرطی و حل دستگاه.", [
        unit("discrete", 14, "رابطه، تابع و ناوردا", "d_relations d_functions d_invariants d_number", "پیش‌نیاز پیمانه و رابطه را تثبیت کنید."),
        unit("algorithms", 16, "بازگشت و درستی", "a_recurrence a_divide a_correct", "رابطهٔ زمانی و اثبات درستی را جدا بنویسید."),
        unit("probability", 12, "احتمال شرطی و بیز", "s_conditional s_bayes", "مخرج شرط و نرخ پایه را صریح مشخص کنید."),
        unit("linear", 10, "حذف گاوسی و رتبه", "l_gauss l_rank", "جواب دستگاه را به رتبه ربط دهید."),
        unit("english", 4, "انگلیسی موازی", "", "درک جمله و خلاصهٔ بند؛ بدون آزمون."),
    ]),
    week(3, "۱۶ تا ۲۲ مهر", "شمارش و ساختار", "ساختمان داده آغاز می‌شود و جست‌وجوی هوش مصنوعی به آن متصل می‌شود.", [
        unit("discrete", 10, "شمارش پایه", "d_counting d_inclusion d_pigeonhole", "نوع شمارش را پیش از فرمول‌گذاری تشخیص دهید."),
        unit("algorithms", 14, "ساختار خطی و مرتب‌سازی", "a_arrays a_stackqueue a_sort a_select", "عملیات و هزینهٔ هر ساختار را مقایسه کنید."),
        unit("probability", 12, "متغیر تصادفی گسسته", "s_descriptive s_discrete s_expectation", "امید را ابتدا از تعریف به‌دست آورید."),
        unit("linear", 8, "دترمینان و فضا", "l_det l_spaces", "دترمینان را جایگزین رتبه نکنید."),
        unit("ai", 8, "عامل و جست‌وجوی ناآگاهانه", "i_agents i_uninformed", "حالت، عمل و هدف را دقیق تعریف کنید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(4, "۲۳ تا ۲۹ مهر", "درخت و تخمین", "مرز روش‌های داده‌ساختاری و جست‌وجوی آگاهانه روشن می‌شود.", [
        unit("discrete", 8, "بازگشت و تابع مولد", "d_recurrence d_generating", "حل بازگشت را از شمارش حالت متمایز کنید."),
        unit("algorithms", 15, "درخت، هیپ و هش", "a_bst a_balanced a_heap a_hash a_amortized", "بدترین، میانگین و سرشکن را جداگانه ثبت کنید."),
        unit("probability", 11, "واریانس و توزیع‌ها", "s_variance s_distributions", "شرایط کاربرد هر توزیع را بنویسید."),
        unit("linear", 8, "تبدیل و تعامد", "l_linear l_orthogonality", "هسته، تصویر و تعامد را با مثال هندسی بخوانید."),
        unit("ai", 10, "جست‌وجوی آگاهانه", "i_informed i_optimality", "شرط بهینگی و سازگاری تخمین را تفکیک کنید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(5, "۳۰ مهر تا ۶ آبان", "گراف و قید", "پیمایش گراف، متغیر پیوسته و جست‌وجوی خصمانه.", [
        unit("discrete", 8, "گراف و درخت", "d_graph d_trees", "خواص ساختاری را به پیمایش الگوریتمی وصل کنید."),
        unit("algorithms", 14, "نمایش و پیمایش گراف", "a_graphrep a_bfsdfs a_topological", "پیش‌شرط و هزینهٔ هر پیمایش را بنویسید."),
        unit("probability", 10, "پیوسته و مشترک", "s_continuous s_joint", "چگالی را با احتمال نقطه‌ای خلط نکنید."),
        unit("linear", 8, "تصویر و کمترین مربعات", "l_projection l_leastsquares", "راه‌حل را هم هندسی و هم جبری بررسی کنید."),
        unit("ai", 12, "بازی و مسئلهٔ قید", "i_games i_csp", "هرس و انتشار محدودیت را با مثال حل‌شده ببینید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(6, "۷ تا ۱۳ آبان", "مسیر و استنتاج", "الگوریتم‌های مسیر، امید شرطی و منطق در هوش مصنوعی.", [
        unit("discrete", 6, "احتمال گسسته", "d_dprob", "پیوند شمارش و احتمال را جمع‌بندی کنید."),
        unit("algorithms", 14, "درخت پوشا، مسیر و حریصانه", "a_mst a_shortest a_greedy", "شرط وزن‌ها و اثبات انتخاب حریصانه مهم است."),
        unit("probability", 10, "امید شرطی و تبدیل متغیر", "s_condexp s_transform", "توزیع حاصل را با پشتیبان درست محاسبه کنید."),
        unit("linear", 10, "ویژه‌مقدار و قطری‌سازی", "l_eigen l_diagonal", "تفسیر تبدیل را همراه محاسبه بخوانید."),
        unit("ai", 12, "بازنمایی دانش", "i_prop i_fol", "منطق محمولات اینجا ابزار استنتاج است، نه نظریهٔ زبان‌ها."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(7, "۱۴ تا ۲۰ آبان", "طراحی و برآورد", "روش‌های پیشرفتهٔ طراحی و آمار استنباطی آغاز می‌شوند.", [
        unit("algorithms", 15, "برنامه‌ریزی پویا، جریان و کران", "a_dp a_flow a_lower", "حالت، گذار و گواه درستی را کامل بنویسید."),
        unit("probability", 12, "حدها و نمونه‌گیری", "s_llnclt s_sampling", "فرض‌های تقریب و نمونه‌گیری را مشخص کنید."),
        unit("linear", 8, "تجزیهٔ مقدار منفرد", "l_svd", "تنها پیوند لازم با مبانی جبر خطی و هوش مصنوعی."),
        unit("ai", 17, "استنتاج و برنامه‌ریزی", "i_inference i_planning", "قواعد استنتاج و حالت‌های برنامه‌ریزی را جدا کنید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(8, "۲۱ تا ۲۷ آبان", "عدم قطعیت", "احتمال و جبر خطی در هوش مصنوعی به کار می‌آیند.", [
        unit("discrete", 4, "مرور گراف و شمارش", "d_graph d_counting", "شکاف‌های تعریفی دور نخست را اصلاح کنید."),
        unit("algorithms", 14, "تصادفی و رشته", "a_random a_string", "امید هزینه و شرط الگوریتم‌ها را بسنجید."),
        unit("probability", 12, "برآورد و آزمون فرض", "s_estimation s_hypothesis", "خطای نوع اول و دوم را با مثال حل‌شده ببینید."),
        unit("ai", 22, "بیز، شبکه و تصمیم", "i_bayes i_bn i_decision", "استقلال شرطی را با ساختار شبکه بررسی کنید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(9, "۲۸ آبان تا ۴ آذر", "یادگیری", "یادگیری پایه بر زمینهٔ احتمال و جبر خطی.", [
        unit("algorithms", 12, "بازخوانی طراحی الگوریتم", "a_greedy a_dp a_correct", "روش‌ها را با مسئله‌های تشریحی ترکیب کنید."),
        unit("probability", 12, "رگرسیون و مارکوف مقدماتی", "s_regression s_markov", "محدودهٔ عنوان آمار مهندسی حفظ می‌شود."),
        unit("linear", 4, "بازخوانی ویژه‌مقدار", "l_eigen l_projection", "کاربرد را به مفاهیم پایه برگردانید."),
        unit("ai", 24, "چارچوب یادگیری و دسته‌بندی", "i_learning i_classification", "تعمیم و ارزیابی را همراه الگوریتم بخوانید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(10, "۵ تا ۱۱ آذر", "تکمیل هوش مصنوعی", "موضوع‌های اصلی بسته می‌شوند؛ مرور هنوز تشریحی است.", [
        unit("discrete", 8, "یکپارچه‌سازی اثبات", "d_proof d_induction d_recurrence", "برهان‌ها را با زبان دقیق بازنویسی کنید."),
        unit("algorithms", 12, "یکپارچه‌سازی ساختارها", "a_sort a_hash a_bfsdfs", "جدول انتخاب روش و شرط‌هایش بسازید."),
        unit("probability", 12, "یکپارچه‌سازی احتمال", "s_bayes s_expectation s_hypothesis", "شرط‌ها و فرض‌ها را در هر روش کنترل کنید."),
        unit("ai", 20, "خوشه‌بندی، شبکهٔ عصبی و ارزیابی", "i_clustering i_neural i_eval", "عمق این فصل‌ها با دفترچه‌های مرتبط بازبینی می‌شود."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
    week(11, "۱۲ تا ۱۸ آذر", "بستن دور نخست", "جاهای مبهم با مثال‌های حل‌شده رفع می‌شوند و آمادگی مرحلهٔ بعد ثبت می‌شود.", [
        unit("discrete", 8, "مرور مرزهای گسسته", "d_relations d_generating d_trees", "فهرست ابهام‌ها را به توضیح حل‌شده تبدیل کنید."),
        unit("algorithms", 12, "مرور تحلیل و طراحی", "a_asym a_amortized a_shortest a_flow", "شرط‌های اعتبار پاسخ‌ها را مرور کنید."),
        unit("probability", 10, "مرور توزیع و استنباط", "s_joint s_condexp s_estimation", "مفروضات و دام‌های رایج را ثبت کنید."),
        unit("linear", 8, "مرور فضا و تجزیه", "l_rank l_spaces l_diagonal", "ارتباط رتبه، بعد و مقادیر ویژه را ببینید."),
        unit("ai", 14, "مرور جست‌وجو و استنتاج", "i_informed i_bn i_learning", "مرز کاربرد روش‌ها را روشن کنید."),
        unit("english", 4, "انگلیسی موازی", "", "خواندن متن علمی؛ بدون آزمون."),
    ]),
]

# Two high-return exam subjects have their own chapters and hours every week.
# Keep the 56-hour ceiling by taking time from the largest existing core unit.
programming_path = [
    ("نوع داده و جریان اجرا", "p_types p_flow"),
    ("تابع و آرایه", "p_functions p_arrays"),
    ("رشته و بازگشت", "p_strings p_recursion"),
    ("اشاره‌گر و حافظه", "p_pointers p_memory"),
    ("نمایش داده و بیت", "p_rep p_bitwise"),
    ("ساختار و ردگیری", "p_structs p_trace"),
    ("مرور حلقه و بازگشت", "p_flow p_recursion"),
    ("مرور اشاره‌گر و حافظه", "p_pointers p_memory"),
    ("مرور خطاهای مرزی", "p_trace"),
    ("مرور عملگرهای بیتی", "p_bitwise"),
    ("مرور ساختار و تابع", "p_structs p_functions"),
]
logic_path = [
    ("مبنا، جبر بولی و گیت", "g_number g_boolean g_gates"),
    ("ساده‌سازی و مدار ترکیبی", "g_kmap g_combin"),
    ("مدار حسابی و گزینش", "g_arithmetic g_mux"),
    ("لچ و فلیپ‌فلاپ", "g_latch g_ff"),
    ("ثبات و شمارنده", "g_register g_counter"),
    ("ماشین حالت و زمان‌بندی", "g_fsm g_timing"),
    ("مخاطره و حافظه", "g_hazards g_memory"),
    ("مرور ساده‌سازی و ماشین حالت", "g_kmap g_fsm"),
    ("مرور مدار ترکیبی", "g_combin"),
    ("مرور تأخیر و مسیر بحرانی", "g_timing"),
    ("مرور شمارنده و حالت", "g_counter g_fsm"),
]
for index, entry in enumerate(weeks):
    additional_hours = 4 if index < 8 else 2
    for subject, path in (("programming", programming_path), ("logic", logic_path)):
        title, ids = path[index]
        entry["units"].insert(-1, unit(subject, additional_hours, title, ids,
            "تعریف و مثال‌های حل‌شده را بخوانید؛ در دور نخست آزمون نداریم."))
    for _ in range(2 * additional_hours):
        candidates = [u for u in entry["units"] if u["subject"] not in
                      {"programming", "logic", "english"} and u["hours"] > 4]
        assert candidates, entry["number"]
        max(candidates, key=lambda u: u["hours"])["hours"] -= 1
    entry["totalHours"] = sum(u["hours"] for u in entry["units"])

sources = [
    ("فهرست مواد آزمون ۱۴۰۶", "https://phdtest.ir/wp-content/uploads/2026/03/Sarfasl-Zarayeb-Manbe-Konkoor-PhD-1406-PhdTest.pdf#page=23"),
    ("مخزن دفترچه‌های آزمون", "https://github.com/bheydari721rn24/Phd-Exam-CSE"),
    ("ریاضیات گسستهٔ ام‌آی‌تی، ۲۰۲۴", "https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/"),
    ("مبانی برنامه‌سازی با C در CS50", "https://cs50.harvard.edu/x/weeks/1/"),
    ("الگوریتم ام‌آی‌تی", "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/"),
    ("احتمال ام‌آی‌تی", "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"),
    ("احتمال هاروارد", "https://stat110.hsites.harvard.edu/"),
    ("جبر خطی ام‌آی‌تی", "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"),
    ("مدار منطقی در ام‌آی‌تی", "https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/"),
    ("هوش مصنوعی ام‌آی‌تی", "https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/"),
]

data = {
    "updatedLabel": "۲ مهر ۱۴۰۵ · نسخهٔ سوم",
    "method": "هفت درس اولویت اول شامل برنامه‌سازی و مدار منطقی با ساعت مستقل‌اند. ساعت هر هفته ۵۶ است و چهار ساعت انگلیسی موازی دارد. این فصل‌بندی یک نقشهٔ آموزشی قابل بازبینی است؛ سازمان سنجش ریزفصل و تعداد سؤال هر درس را اعلام نکرده است.",
    "strategy": {
        "core": "هفت درس اولویت اول: مبانی برنامه‌سازی، مدار منطقی، ساختمان داده و الگوریتم، گسسته، آمار و احتمال، جبر خطی و هوش مصنوعی.",
        "support": "برنامه‌سازی و مدار منطقی هر هفته ساعت و فصل مستقل دارند؛ پیوندشان با الگوریتم و معماری هم در جزوه‌ها مشخص می‌شود.",
        "deferred": "سیستم‌عامل و معماری کامپیوتر در اولویت دوم، پس از دور نخست و با بازبینی زمان باقی‌مانده.",
        "excluded": "نظریهٔ زبان‌ها طبق خواستهٔ شما از برنامه حذف شده است.",
        "english": "انگلیسی هر هفته ۴ ساعت موازی پیش می‌رود.",
        "reviewGate": "پایان هفتهٔ ششم: ساعت هر هفت درس با پیشرفت واقعی شما و تحلیل دفترچه‌های مرتبط بازبینی می‌شود."
    },
    "subjects": subjects, "topics": topics, "weeks": weeks,
    "sources": [{"label": label, "url": url} for label, url in sources],
}

all_ids = set(topics)
used = [topic_id for w in weeks for u in w["units"] for topic_id in u["topicIds"]]
assert all(topic_id in all_ids for topic_id in used)
assert all_ids == set(used), sorted(all_ids - set(used))
assert all(w["totalHours"] == 56 for w in weeks)
assert all({u["subject"] for u in w["units"]} <= set(subjects) | {"english"} for w in weeks)
assert len(weeks) == 11
assert sum(w["totalHours"] for w in weeks) == 616

target = ROOT / "dist" / "schedule.json"
target.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"{len(weeks)} weeks, {len(topics)} topics, {sum(w['totalHours'] for w in weeks)} hours -> {target}")
