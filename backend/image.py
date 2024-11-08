
import os
import openai
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get('DALLE')

def Generate_image(story_type,sub_type, story):

    if "جدة" in story or "امرأة" in story or "الأم" in story:
        narrator = "امرأة مسنّة سعودية"
    elif "جد" in story or "رجل" in story or "الأب" in story:
        narrator = "رجل مسنّ سعودي"
    else:
        narrator = "شخص مسنّ سعودي"


    if sub_type =="قصص الأنبياء":
        prompt = f"استخدم العناصر البصرية فقط من هذه القصة لإنشاء مشهد مرسوم. تجاهل التفاصيل النصية التي لا يمكن تصويرها، وركز فقط على الشخصيات والأحداث التي يمكن تمثيلها في الرسم.\n\nالقصة: {story}\n\nرسم توضيحي يظهر {narrator} يجلس في مكان دافئ وجميل ويروي قصة عن نبي لفتاة صغيرة تستمع بانتباه. يظهر الراوي وهو يرتدي ملابس سعودية تقليدية تعكس الثقافة الإسلامية، بينما تُظهر الفتاة تعابير وجه تعكس الفضول والاحترام."

    elif sub_type =="قصص الصحابة":
        prompt = f"استخدم العناصر البصرية فقط من هذه القصة لإنشاء مشهد مرسوم. تجاهل التفاصيل النصية التي لا يمكن تصويرها، وركز فقط على الشخصيات والأحداث التي يمكن تمثيلها في الرسم.\n\nالقصة: {story}\n\nرسم توضيحي لـ {narrator} يجلس في مكان دافئ، يروي قصة عن صحابي لشخص صغير. يظهر الراوي بملابس سعودية تاريخية تعكس الثقافة الإسلامية، بينما يُظهر المستمع تعابير الاحترام والاهتمام."

    elif sub_type =="العبادات":
        prompt = f"استخدم العناصر البصرية فقط من هذه القصة لإنشاء مشهد مرسوم. تجاهل التفاصيل النصية التي لا يمكن تصويرها، وركز فقط على الشخصيات والأحداث التي يمكن تمثيلها في الرسم.\n\nالقصة: {story}\n\nرسم توضيحي لمشهد ديني يُظهر {narrator} يشرح عبادة معينة لطفل صغير، مثل الصلاة أو الصوم. تُظهر البيئة المحيطة أجواءً تاريخية سعودية وعناصر ثقافية، مثل سجادة الصلاة وأدوات الصيام، وتُبرز تركيز الطفل واهتمامه."


    elif story_type == 'خيالية':
        prompt = f"استخدم العناصر البصرية فقط من هذه القصة لإنشاء مشهد مرسوم قصة مصورة من عدة صور. تجاهل التفاصيل النصية التي لا يمكن تصويرها، وركز فقط على الشخصيات والأحداث التي يمكن تمثيلها في الرسم.\n\nالقصة: {story}\n\nرسم خيالي وساحر لشخصيات ومخلوقات خيالية، مع ألوان زاهية ومناظر طبيعية سريالية تُظهر جوًا من الأحلام والسحر."

    elif story_type == 'تعليمية':
        prompt = f"استخدم العناصر البصرية فقط من هذه القصة لإنشاء مشهد مرسوم قصة مصورة من عدة صور. تجاهل التفاصيل النصية التي لا يمكن تصويرها، وركز فقط على الشخصيات والأحداث التي يمكن تمثيلها في الرسم.\n\nالقصة: {story}\n\nرسم توضيحي لبيئة تعليمية مبهجة، يُظهر أطفالًا ومعلمين يتفاعلون بطريقة مبهجة مع الألوان والأدوات التعليمية."

    elif story_type == 'واقعية':
        prompt = f"استخدم العناصر البصرية فقط من هذه القصة لإنشاء مشهد مرسوم قصة مصورة من عدة صور. تجاهل التفاصيل النصية التي لا يمكن تصويرها، وركز فقط على الشخصيات والأحداث التي يمكن تمثيلها في الرسم.\n\nالقصة: {story}\n\nرسم توضيحي لأشخاص في مشهد يومي واقعي، في بيئة منزلية أو عمل، يظهر فيها التعبير الواقعي والحياة اليومية."

    elif story_type == 'حضارات و تراث السعودية':
        prompt = f"استخدم العناصر البصرية فقط من هذه القصة لإنشاء مشهد مرسوم قصة مصورة من عدة صور. تجاهل التفاصيل النصية التي لا يمكن تصويرها، وركز فقط على الشخصيات والأحداث التي يمكن تمثيلها في الرسم.\n\nالقصة: {story}\n\nرسم توضيحي يعرض عناصر من التراث السعودي، مع العمارة والملابس التقليدية، وتفاصيل دقيقة تبرز الثقافة السعودية."

    prompt += ' أنشأ صورة مباشره'
    prompt += ' اذا كان احد الشخصيات محميه انشأ صور قريبه بالشخصيات الاخرى'
    openai.api_key = key
    client = openai.Client(api_key=key)

    story_prompt = (
        f"قم بتحليل القصة التالية واستخراج الأحداث الرئيسية لإنشاء ستوري بورد. "
        "وإذا لم تستطيع انشاء ستوري بورد انشأ صوره تعبر عن القصة. "
        f"انِشأ صور فقط , لاتكتب على الصور: {prompt}"
    )

    response = client.images.generate(
        model="dall-e-3",
        prompt=story_prompt,
        size="1024x1024",
        n=1,
    )

    image_url = response.data[0].url
    return image_url




