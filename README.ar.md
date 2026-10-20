<div dir="rtl">

# frontend-noslop

حزمة هندسية احترافية لنماذج ووكلاء الذكاء الاصطناعي (AI Coding Agents). تفرض توجهاً بصرياً مقصوداً، ومكتبات واجهات معتمدة، ونظام ألوان قائم على علم الـ OKLCH، وبوابات فحص صارمة لمنع توليد الواجهات النمطية والمبتذلة (AI Slop).

<p align="right">
  <a href="README.md">English (الإنجليزية)</a> • <b>العربية</b>
</p>

[![License: MIT](https://img.shields.io/badge/الرخصة-MIT-black.svg?style=flat-square)](LICENSE)
[![Skills.sh](https://img.shields.io/badge/skills.sh-معتمد-black?style=flat-square)](https://skills.sh)
[![متوافق مع Claude Code](https://img.shields.io/badge/Claude%20Code-متوافق-black?style=flat-square)](https://anthropic.com)
[![متوافق مع Antigravity](https://img.shields.io/badge/Antigravity-أصلي-black?style=flat-square)](https://github.com)

```bash
# تثبيت الحزمة على جميع الوكلاء بأمر واحد
npx skills add AhmadJalhoom20/frontend-noslop -g -y
```

---

## المشكلة: الواجهات النمطية للذكاء الاصطناعي (AI Slop)

تعتمد نماذج الذكاء الاصطناعي بطبيعتها على المتوسط الإحصائي لبيانات التدريب. عند طلب بناء واجهة مستخدم دون فرض قيود صارمة، ينحدر النموذج تلقائياً إلى كليشيهات متكررة:

1. **لوحة الألوان المكررة:** خلفيات داكنة موحدة مع تدرجات لونية عشوائية (`from-purple-500 to-cyan-500`) ووهج نيون ضبابي.
2. **قالب البطاقات الثلاثية:** شبكة مكونة من 3 بطاقات متطابقة تحتوي أيقونات في مربعات باستيل ونصوص تسويقية فارغة.
3. **النصوص الروبوتية:** عبارات رنانة بلا معنى (*"ارتقِ بأعمالك بسلاسة مع الجيل القادم"*).
4. **تجاهل الحالات الأساسية:** إهمال كامل لحالات التحميل (Loading Skeletons)، والحالات الفارغة (Empty States)، ومعالجة الأخطاء.
5. **فوضى الـ HTML:** استخدام وسوم `div` مع أحداث `onClick` وتجاهل إمكانية الوصول والتنقل عبر لوحة المفاتيح ومعايير ARIA.

تعمل **`frontend-noslop`** كطبقة تنظيمية فوق مسار عمل النموذج؛ حيث تستبدل الأنماط العشوائية بمسار مهندس واجهات خبير.

---

## مقارنة برمجية واقعية

### الكود الافتراضي للذكاء الاصطناعي (النمط المبتذل)
```tsx
// ناتج الموديل الافتراضي بدون قيود
export default function Hero() {
  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col items-center justify-center p-8">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-purple-500/20 blur-3xl rounded-full" />
      <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
        Streamline Your Workflow
      </h1>
      <p className="mt-4 text-slate-400 max-w-md text-center">
        Unlock next-gen efficiency with our cutting-edge AI-powered platform.
      </p>
      <button className="mt-6 px-6 py-3 rounded-xl bg-purple-600 hover:bg-purple-500 transition shadow-lg shadow-purple-500/25">
        Get Started Free ✨
      </button>
    </div>
  );
}
```

### مع `frontend-noslop` (مستوى استوديوهات التصميم العالمية)
```tsx
// كود منضبط: رموز تصميم واضحة، دلالات HTML صحيحة، وحالات وصول مكتملة
import { ArrowRight } from "lucide-react";

export default function Hero() {
  return (
    <section className="relative mx-auto max-w-5xl px-6 py-24 sm:py-32">
      <header className="max-w-2xl">
        <p className="font-mono text-xs uppercase tracking-widest text-[var(--color-muted)]">
          بنية التدقيق والامتثال
        </p>
        <h1 className="mt-4 font-serif text-4xl sm:text-6xl tracking-tight text-[var(--color-foreground)] leading-[1.08]">
          التحقق المالي الحتمي للأنظمة فائقة السرعة.
        </h1>
        <p className="mt-6 text-base sm:text-lg leading-relaxed text-[var(--color-muted)]">
          تحقق مشفر من مسارات معالجة البيانات حتى أجزاء المللي ثانية. صفر استهلاك تشغيلي إضافي، ودعم أصلي لـ OpenTelemetry.
        </p>
      </header>

      <div className="mt-10 flex flex-wrap items-center gap-4">
        <a
          href="/docs"
          className="inline-flex h-11 items-center justify-center rounded-sm bg-[var(--color-primary)] px-5 text-sm font-medium text-[var(--color-primary-contrast)] transition-colors hover:bg-[var(--color-primary-hover)] focus-visible:outline-2 focus-visible:outline-offset-2"
        >
          قراءة وثيقة المعمارية
          <ArrowRight className="mr-2 h-4 w-4" aria-hidden="true" />
        </a>
      </div>
    </section>
  );
}
```

---

## المعمارية: 8 محركات مدمجة في مسار واحد

لا تعيد `frontend-noslop` اختراع الأدوات؛ بل تدمج **أقوى 8 مهارات عالمية** في خط أنابيب واحد متماسك:

```
[ المرحلة 1: تحديد الهوية البصرية ] ← frontend-design + frontend-design-deslop
             ↓
[ المرحلة 2: ضبط رموز التصميم ]     ← antislop-ui + DESIGN.md (نظام OKLCH)
             ↓
[ المرحلة 3: انتقاء المكتبات ]       ← pick-ui-library (المكتبات المعتمدة)
             ↓
[ المرحلة 4: التنفيذ البرمجي ]       ← react-best-practices + تغطية الحالات الـ 5
             ↓
[ المرحلة 5: بوابة فحص الجودة ]      ← impeccable (/critique, /polish) + no-ai-slop
```

| الأداة | المصدر | الدور الوظيفي في المنظومة |
|---|---|---|
| `impeccable` | Paul Bakaus (Google سابقاً) | فرض الحد الأدنى للجودة وأوامر المراجعة التلقائية (`/critique`, `/polish`, `/audit`). |
| `frontend-design` | Anthropic | فرض هوية جمالية صريحة (مثل: Editorial Brutalism، Luxury Minimal) قبل كتابة الكود. |
| `design-taste-frontend` | Leonxlnx | ضبط التوازن البصري، ومقياس الخطوط الرياضي، وتوتر المساحات البيضاء. |
| `frontend-design-deslop` | Samber | إزالة أنماط Tailwind المكررة وتوليد رموز ألوان OKLCH وملف `DESIGN.md`. |
| `antislop-ui` | Miqdad Badjuber | فرض قواعد بصرية تمنع التدرجات البنفسجية المبتذلة والبطاقات المكررة. |
| `no-ai-slop` | Peter Yang | تدقيق النصوص وصياغة رسائل واقعية وبشرية خالية من حشو الذكاء الاصطناعي. |
| `pick-ui-library` | Emil Kowalski | ترشيح مكتبات تفاعلية خفيفة غير مكسوة بأنماط جاهزة وسهلة الوصول. |
| `react-best-practices` | Vercel Engineering | معمارية Server Components، منع قفزات الواجهة (Zero CLS)، واستخدام Streaming. |

---

## حزمة المكونات المعتمدة

نلتزم بمعايير **Emil Kowalski** لانتقاء المكتبات التفاعلية:

- **المكونات الأساسية وإمكانية الوصول:** [Radix UI](https://www.radix-ui.com/) أو [Base UI](https://base-ui.com/)
- **الإشعارات المنبثقة:** [Sonner](https://sonner.emilkowal.ski/)
- **الأدراج السفلية للأجهزة الذكية:** [Vaul](https://vaul.emilkowal.ski/)
- **قائمة الأوامر ولوحة المفاتيح:** [CMDK](https://cmdk.paco.me/)
- **الحركة والفيزياء:** [Motion (Framer)](https://motion.dev/)
- **القوائم الافتراضية الضخمة:** [React Virtuoso](https://virtuoso.dev/)

---

## طرق التثبيت والاستخدام

### 1. عبر أداة Skills CLI (لجميع الوكلاء)
تثبيت عام على Claude Code، Cursor، Copilot، Antigravity، Cline، و Codex:

```bash
npx skills add AhmadJalhoom20/frontend-noslop -g -y
```

### 2. في Google Antigravity / Gemini CLI
```bash
git clone https://github.com/AhmadJalhoom20/frontend-noslop.git ~/.gemini/config/plugins/frontend-noslop
```

### 3. في متجر إضافات Claude Code
```bash
/plugin marketplace add AhmadJalhoom20/frontend-noslop
/plugin install frontend-noslop
```

---

## بوابة فحص الجودة (The Verification Gate)

قبل تسليم الكود للمستخدم أو اعتماده للإنتاج، يجب استيفاء 5 شروط إلزامية:

1. **الهدف من الألوان:** منع أي تدرج لوني مجرد من الوظيفة الهيكلية.
2. **اكتمال الحالات البرمجية:** تغطية الحالات الـ 5 كاملة (الفارغة، التحميل الهيكلي Skeleton، النجاح، الخطأ مع زر إعادة المحاولة، والتعطيل).
3. **إمكانية الوصول (A11y):** قابلية التنقل الكامل بلوحة المفاتيح عبر زر `Tab` ومؤشرات تركيز واضحة ونسب تباين WCAG 2.1 AA.
4. **التجاوب الهندسي:** تصميم مرن ومختبر من مقاسات الهواتف (360px) حتى الشاشات العريضة دون شريط تمرير أفقي.
5. **دقة النصوص:** إزالة كافة الكلمات المستهلكة (*"سلس"*, *"ارتقِ"*, *"الجيل القادم"*, *"افتح آفاق"*).

---

## المساهمة في المشروع

نرحب بمساهمات المجتمع البرمجي، وتحديثات القواعد، والإبلاغ عن المشكلات. عند اقتراح قاعدة جديدة، يُرجى تضمين عينات كود واقعية توضح النمط المبتذل وكيفية حله.

## الرخصة

مرخص تحت رخصة **MIT**. راجع ملف [`LICENSE`](LICENSE) للمزيد من التفاصيل.

<br/>

<div align="center">
  <sub>طُوّر بعناية بواسطة <a href="https://github.com/AhmadJalhoom20">أحمد جلهوم (Ahmad Jalhoom)</a>. كود نقي وواجهات بشرية متقنة.</sub>
</div>

</div>
