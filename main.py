import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():

    # تحميل نماذج الذكاء الاصطناعي المحفوظة (التنبؤ + التصنيف)
    reg_model = joblib.load("student_model.pkl")
    clf_model = joblib.load("classification_model.pkl")

    # قراءة بيانات الاختبار من ملف CSV
    df = pd.read_csv("new_data.csv")

    # تحويل الأعمدة النصية إلى أرقام حتى يقدر النموذج يتعامل معها
    le = LabelEncoder()
    for col in df.select_dtypes(include="object").columns:
        df[col] = le.fit_transform(df[col].astype(str))

    # المدخلات: كل الأعمدة ما عدا Exam_Score
    X_reg = df.drop("Exam_Score", axis=1)
    predicted_scores = reg_model.predict(X_reg)

    # إضافة نتيجة التنبؤ كعمود جديد
    df["Predicted_Exam_Score"] = predicted_scores

    # المدخلات: نفس الأعمدة لكن بدون Exam_Score وبدون عمود التنبؤ
    X_clf = df.drop(["Exam_Score", "Predicted_Exam_Score"], axis=1)
    predicted_groups = clf_model.predict(X_clf)

    # تحويل أرقام التصنيف إلى كلمات مفهومة
    mapping = {0: "Fail", 1: "Pass", 2: "Excellent"}
    df["Predicted_Group"] = pd.Series(predicted_groups).map(mapping)

    # عرض أول 5 صفوف للتأكد
    print(df.head())

    # حفظ النتائج بملف جديد
    df.to_csv("results_on_kaggle_data.csv", index=False)
    print("\nResults saved to results_on_kaggle_data.csv")

if __name__ == "__main__":
    main()