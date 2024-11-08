import os
from ibm_watsonx_ai.foundation_models import Model
from dotenv import load_dotenv

load_dotenv()
client = os.environ.get('ALLAM')

model_id = "sdaia/allam-1-13b-instruct"
project_id="205151a7-1420-48e6-8e63-790db4af6843"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 1500,
    "repetition_penalty": 1
}

def get_credentials():
    return {
        "url": "https://eu-de.ml.cloud.ibm.com",
        "apikey": client
    }

model = Model(
	model_id = model_id,
	params = parameters,
	credentials = get_credentials(),
	project_id = project_id,
	)

prompt_input_instruction = """<<SYS>>
ملاحظات:
- ابدأ بعنوان للقصه
- إذا كانت القصة خيالية أو واقعية أو تعليمية، يجب أن يكون {اسم الطفل او الطفله} بطل القصة، وتدور الأحداث حول مغامراته أو تجاربه أو تعلمه.
- يجب أن تكون القصة مبسطة وواضحة بما يناسب طفل بعمر {عمر الطفل او الطفله}.
- في القصص الخيالية، يجب أن تتضمن عناصر الإبداع والخيال مثل مخلوقات غريبة أو عوالم سحرية، مع دور رئيسي للبطل {اسم الطفل او الطفله}. الا اذا كان في شخصيه معروفه فادخل الشخصيه الى القصه.
- اذا كان يوجد شخصيه محدده فأدخل الشخصيه في  سرد القصه
- في القصص التعليمية، الهدف هو توصيل معلومة أو درس في نهاية القصة بطريقة ممتعة وجذابة، ويجب أن يتفاعل {اسم الطفل او الطفله} مع المعلومات في سياق القصة.
- في القصص الإسلامية، يمكن استخدام أحداث من السيرة النبوية أو قصص الأنبياء مع التركيز على الأخلاق والقيم الإسلامية.
- في قصص الحضارة والتراث السعودي، يجب تسليط الضوء على تاريخ وتراث المملكة العربية السعودية بشكل يتماشى مع مستوى الطفل، مع تركيز خاص على تقاليد وعادات المملكة.
كن دائماً طيب القلب ومحباً للخير.
-لاتنهي القصه بسؤال المطفل عن اسأله او مااذاكان بربد قصه اخرى
- يجب ان تنوع في طريقة سرد وحبكة القصه في كل مره حتى لو كان المدخل نفسه.
-لاتكرر القصة نفسها.
- يجب ان تلتزم بنوع القصه في كل مرة.


نص القصة المقترح:
 </s><s> [INST]"""

def generateStory(prompt):
  formattedprompt = f"""<s> [INST] {prompt} [/INST]"""
  prompt = f"""{prompt_input_instruction}{formattedprompt}"""
  generated_response_story = model.generate_text(prompt=prompt, guardrails=False)
  return generated_response_story
