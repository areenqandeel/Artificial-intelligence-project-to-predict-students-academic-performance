Student Academic Performance Prediction System (AI Project)

1) فكرة المشروع:
هذا المشروع يختبر نموذج ذكاء اصطناعي للتعامل مع بيانات أداء الطلاب.
يقوم المشروع بعمل وظيفتين:
- Regression: التنبؤ بالدرجة النهائية للطالب (Predicted_Exam_Score).
- Classification: تصنيف الطالب إلى (Fail / Pass / Excellent) (Predicted_Group).

2) الملفات داخل المشروع:
- main.py
  الملف الرئيسي لتشغيل المشروع. يقوم بتحميل نماذج الذكاء الاصطناعي (pkl)
  ثم يقرأ ملف البيانات (CSV) ويخرج النتائج.

- student_model.pkl
  نموذج التنبؤ بالدرجة النهائية (Regression model).

- classification_model.pkl
  نموذج التصنيف (Classification model).

- new_data.csv
  ملف بيانات للتجربة (مدخلات المشروع).

- results_on_kaggle_data.csv
  ملف النتائج الذي يتم توليده بعد تشغيل main.py (Output).

3) كيفية تشغيل المشروع:
أ) التأكد من تثبيت المكتبات المطلوبة:
pip install -r requirements.txt

ب) تشغيل الملف الرئيسي:
python main.py

4) مخرجات المشروع:
بعد التشغيل سيتم:
- طباعة أول 5 صفوف من البيانات مع الأعمدة الجديدة:
  Predicted_Exam_Score و Predicted_Group
- حفظ ملف جديد باسم:
  results_on_kaggle_data.csv

5) ملاحظة مهمة:
يجب أن يكون ملف new_data.csv يحتوي على نفس الأعمدة التي تم تدريب النماذج عليها

(وبنفس أسماء الأعمدة) حتى يعمل التنبؤ بدون أخطاء.
