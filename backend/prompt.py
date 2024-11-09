#قصص إسلاميه
import random
import json

def get_age_group(user_age):
    if 3 <= user_age <= 5:
        return '3-5'
    elif 5 < user_age <= 8:
        return '5-8'
    elif 8 < user_age <= 10:
        return '8-10'
    elif 10 < user_age <= 12:
        return '10-12'
    else:
        return 'غير محددة'


def complete_user_prompt_islamic_stories(
    template_parameters,
    sub_type,
    user_input,
    user_name,
    user_age
):
    # Story type:
    story_type = 'قصص إسلامية. '
    
    prompt = story_type
    age_group = get_age_group(user_age)
    if age_group != 'غير محددة':
        prompt += f"القصة موجهة للأطفال بعمر {age_group}. "
    else:
        prompt += f"العمر المدخل {user_age} خارج النطاق المخصص للقصة."

    # Normalize user input to handle different Arabic letters
    normalized_input = user_input.replace("ة", "ه").replace("أ", "ا").replace("ؤ", "و")

    # Check for matches in prophets or companions
    if sub_type == 'الأنبياء':
        found = False
        for character_name in template_parameters['character_prophets']:
            normalized_name = character_name.replace("ة", "ه").replace("أ", "ا").replace("ؤ", "و")
            if normalized_input in normalized_name:
                prompt += f"احكي لي قصة عن النبي {character_name}. "
                motivational_message = (
                    f"{user_name}، تذكر دائمًا أن الأنبياء كانوا قدوة في الصبر والشجاعة والإيمان. "
                    f"كن دائمًا صادقًا وشجاعًا مثل النبي {character_name}."
                )
                found = True
                break

        if not found:
            prompt += f"احكي لي قصة عن {user_input}. "
            motivational_message = (
                f"{user_name}، تذكر دائمًا أن الأنبياء كانوا قدوة في الصبر والشجاعة والإيمان. "
                f"كن دائماً صادقًا وشجاعًا."
            )

    elif sub_type == 'الصحابة':
        found = False
        for character_name in template_parameters['male_companions'] + template_parameters['female_companions']:
            normalized_name = character_name.replace("ة", "ه").replace("أ", "ا").replace("ؤ", "و")
            if normalized_input in normalized_name:
                prompt += f"احكي لي قصة عن الصحابي/الصحابية {character_name}. "
                motivational_message = (
                    f"{user_name}، اقتدِ بالصحابة الأوفياء، فهم كانوا أصدقاء مخلصين للرسول ويمتلكون صفات حميدة "
                    f"مثل الصدق والإخلاص والشجاعة. كن مثل {character_name}، وفياً وصادقاً."
                )
                found = True
                break

        if not found:
            prompt += f"احكي لي قصة عن {user_input}. "
            motivational_message = (
                f"{user_name}، عليك دائمًا أن تختار الخير وتبتعد عن السوء، وأن تكون مخلصًا في أفعالك"
            )

    elif sub_type == 'تعليم العبادات':
        prompt += f"أروي لي قصة تعليمية حول {user_input}. "
        motivational_message = (
            f"{user_name}، تذكر أن العبادات هي طريقنا للتقرب من الله، والالتزام بها يملأ القلب سعادة ورضا. "
            f"اجعل هذه القصة دافعاً للالتزام بالعبادات دائماً."
        )

    else:
        prompt += f"أروي لي قصة عن {user_input}. "
        motivational_message = (
            f"{user_name}، تذكر أن الإيمان والعمل الصالح هما الطريق إلى السعادة والرضا. "
            f"كن دائماً طيب القلب ومحباً للخير."
        )

    prompt += " القصة يجب أن تكون مناسبة للأطفال، وبأسلوب مبسط. القصة يجب أن تكون باللغة العربية الفصحى. بدون تغيير في أحداث القصة الحقيقية."

    # Output JSON structure
    output = {
        "user_name": user_name,
        "story_type": story_type,
        "sub_type": sub_type,
        "user_age": age_group,
        "story_content": prompt,
        "motivational_message": motivational_message,
        "note": "القصة مكتوبة بلغة بسيطة تناسب الأطفال."
    }

    return output
# Template parameters setup
template_params_islamic = {
    'character_prophets': [
        "آدم عليه السلام", "إدريس عليه السلام", "نوح عليه السلام", "هود عليه السلام", "صالح عليه السلام",
        "إبراهيم عليه السلام", "لوط عليه السلام", "إسماعيل عليه السلام", "إسحاق عليه السلام",
        "يعقوب عليه السلام", "يوسف عليه السلام", "شعيب عليه السلام", "أيوب عليه السلام",
        "ذو الكفل عليه السلام", "موسى عليه السلام", "هارون عليه السلام", "داوود عليه السلام",
        "سليمان عليه السلام", "إلياس عليه السلام", "اليسع عليه السلام", "يونس عليه السلام",
        "زكريا عليه السلام", "يحيى عليه السلام", "عيسى عليه السلام", "محمد صلى الله عليه وسلم"
    ],
    'male_companions': [
        "أبو بكر الصديق", "عمر بن الخطاب", "عثمان بن عفان", "علي بن أبي طالب", "سعد بن أبي وقاص",
        "عبد الرحمن بن عوف", "طلحة بن عبيد الله", "الزبير بن العوام", "أبو عبيدة بن الجراح",
        "خالد بن الوليد", "سلمان الفارسي", "بلال بن رباح", "أبو هريرة", "عمار بن ياسر",
        "عبد الله بن مسعود", "زيد بن ثابت", "مصعب بن عمير", "حذيفة بن اليمان", "معاذ بن جبل",
        "عبد الله بن عباس", "عبد الله بن عمر", "عبد الله بن الزبير", "سعد بن معاذ",
        "ثابت بن قيس", "جعفر بن أبي طالب", "عكرمة بن أبي جهل", "أنس بن مالك", "عمرو بن العاص",
        "أبي بن كعب", "عبادة بن الصامت"
    ],
    'female_companions': [
        "خديجة بنت خويلد", "عائشة بنت أبي بكر", "حفصة بنت عمر بن الخطاب", "أم سلمة",
        "فاطمة الزهراء", "أسماء بنت أبي بكر", "أم عمارة", "أم حرام بنت ملحان", "أم رومان",
        "سفانة بنت حاتم الطائي", "سمية بنت خياط", "أم أيمن", "زينب بنت جحش",
        "أم سليم", "أم حبيبة", "سودة بنت زمعة", "ميمونة بنت الحارث", "صفية بنت حيي",
        "جويرية بنت الحارث", "أم كلثوم بنت عقبة"
    ]
}




def complete_user_prompt_Imaginary_stories(user_prompt, user_age, template_parameters, user_name, feature_probability=0.15):
    story_type = "قصص خيالية"
    prompt = story_type
    prompt += f"أحكي لي قصة {user_prompt} \n"

    # Determine the age group and include it in the prompt
    age_group = get_age_group(user_age)
    if age_group != 'غير محددة':
        prompt += f"القصة موجهة للأطفال بعمر {age_group}. "
    else:
        prompt += f"العمر المدخل {user_age} خارج النطاق المخصص للقصة."

    # Template additions with probabilities
    if 'place' in template_parameters and random.random() < feature_probability:
        prompt += f"تجري أحداث القصة في {random.choice(template_parameters['place'])}. "
    if 'ending' in template_parameters:
        prompt += f"نهاية القصة يجب أن تكون {random.choice(template_parameters['ending'])}. "
    if 'dialogue' in template_parameters and random.random() < feature_probability:
        prompt += f"تتضمن القصة {template_parameters['dialogue']}. "
    if 'num_of_characters' in template_parameters:
        prompt += f"عدد الشخصيات في القصة يجب أن يكون {random.choice(template_parameters['num_of_characters'])}. "
    if 'technology' in template_parameters and random.random() < feature_probability:
        prompt += f"تتضمن القصة تقنية مثل {random.choice(template_parameters['technology'])}. "
    elif 'magic' in template_parameters and random.random() < feature_probability:
        prompt += f"تتضمن القصة عنصر سحري مثل {random.choice(template_parameters['magic'])}. "
    if 'alien_species' in template_parameters and random.random() < feature_probability:
        prompt += f"تحتوي القصة على كائن فضائي من نوع {random.choice(template_parameters['alien_species'])}. "
    elif 'fantasy_creatures' in template_parameters and random.random() < feature_probability:
        prompt += f"تحتوي القصة على مخلوق خيالي مثل {random.choice(template_parameters['fantasy_creatures'])}. "
    if 'planet' in template_parameters and random.random() < feature_probability:
        prompt += f"تجري الأحداث على كوكب {random.choice(template_parameters['planet'])}. "
    else:
        prompt += f"تجري الأحداث في {random.choice(template_parameters['country'])}. "
    if 'season' in template_parameters and random.random() < feature_probability:
        prompt += f"الأحداث تدور في فصل {random.choice(template_parameters['season'])}. "
    if 'activity' in template_parameters and random.random() < feature_probability:
        prompt += f"يجب أن تتضمن القصة النشاط التالي: {random.choice(template_parameters['activity'])}. "
    if 'emotion' in template_parameters and random.random() < feature_probability:
        prompt += f"تتضمن القصة شعورًا ب{random.choice(template_parameters['emotion'])}. "
    if 'plot_twist' in template_parameters and random.random() < feature_probability:
        prompt += f"تحتوي القصة على تحول غير متوقع: {random.choice(template_parameters['plot_twist'])}. "

    # Closing motivational statement
    motivational_message = f"تذكر يا {user_name} أن كل مغامرة جديدة تحمل في طياتها درسًا قيمًا. ابقَ فضوليًا، شجاعًا، ومستعدًا لاكتشاف العالم."
    prompt += f"\nالقصة يجب أن تكون باللغة العربية الفصحى وموجهة للأطفال.\n"
    prompt += motivational_message

    # Output structure
    output = {
        "user_name": user_name,
        "story_type": story_type,
        "user_age": user_age,
        "story_content": prompt,
        "motivational_message": motivational_message,
        "note": "القصة مكتوبة بلغة بسيطة تناسب الأطفال."
    }

    return json.dumps(output, ensure_ascii=False, indent=4)


# Template parameters for story elements
template_params = {
'place': ["القلعة", "الغابة السحرية", "مدينة تحت الماء", "جزيرة بعيدة", "الجزيرة العائمة",
          "مختبر علمي متقدم", "مدينة روبوتية", "الغابة المطيرة", "شلال جبلي", "السوق التقليدي", "الفضاء الخارجي"],

'technology': ['روبوت ذكي', 'بوابة زمنية', 'مرآة سحرية', 'آلة الزمن', 'كبسولة الأحلام', 'نظام واقع افتراضي متقدم'],

'magic': ['عصا سحرية', 'تعويذة قديمة', 'مخلوق أسطوري', 'قدرة خارقة للطبيعة', 'بلورة الرؤية', 'كتاب سحري', 'مصباح عتيق'],

'fantasy_creatures': ['تنين', 'جني', 'وحش بحري', 'عملاق', 'طائر ناطق', 'حصان مجنح', 'قزم الغابة', 'شجرة حكيمة'],

'alien_species': ['كائن فضائي صغير الحجم', 'مخلوق خفي في الغابة', 'كائن عجيب تحت البحر', 'كائن مائي لامع'],

'planet': ['كوكب بعيد يشبه الأرض', 'جزيرة غامضة وسط المحيط', 'ساحل غريب يلمع تحت ضوء القمر', 'كوكب فضائي بعيد'],

'country': ['مملكة خيالية', 'مدينة المستقبل', 'الغابة المظلمة', "المدينة العائمة", 'السهل الذهبي', 'القرية السحرية'],

'season': ['الصيف', 'الشتاء', 'الربيع', 'الخريف', 'الربيع العطِر'],

'activity': ['الطيران باستخدام السحر', 'البحث عن كنز مفقود', 'اكتشاف مخلوقات جديدة', 'التواصل مع كائنات ذكية',
             "الغوص في أعماق البحار", "محاربة التنانين", 'التجول في الصحراء بحثًا عن أسرار قديمة', 'التنقل عبر بوابة سحرية'],

'emotion': ['السعادة', 'الدهشة', 'الخوف', 'الفضول', "الإثارة", 'الأمان', 'الحماس'],

'plot_twist': ['اكتشاف أن البطل كان يمتلك قدرة خفية', 'الكائن العجيب يصبح صديقًا', 'يكتشف أن المكان مليء بالأسرار المخفية',
               "يتحول الصديق إلى كائن أسطوري", 'الكنز الحقيقي كان الحكمة', 'المعلم هو مخلوق سحري متنكر']

}


 # قصص تعليمية


def complete_user_prompt_educational_stories(user_input, user_age, user_name):
    story_type = "قصص تعليمية"
    prompt = story_type
    prompt += f'أروي لي قصة عن {user_input}.'

        # Determine the age group and include it in the prompt
    age_group = get_age_group(user_age)
    if age_group != 'غير محددة':
        prompt += f"تكون بأسلوب مبسط ومفهوم للأطفال في فئة العمر {age_group}. "
    else:
        prompt += f"العمر المدخل {user_age} خارج النطاق المخصص للقصة."


    # Topics and educational messages
    topics = {
        "الأرقام": "تعليم الأرقام بطريقة ممتعة",
        "الحروف": "تعليم الحروف الأبجدية",
        "الحيوانات": "تعريف الأطفال بأنواع الحيوانات وأماكن عيشها",
        "النباتات": "تعليم الأطفال عن النباتات وكيفية نموها",
        "الفضاء والكواكب": "شرح مبسط للأطفال عن الكواكب والفضاء"
    }

    educational_messages = {
        "الأرقام": f"تعلم الأرقام يساعد {user_name} على التفكير المنطقي ويؤسس للرياضيات.",
        "الحروف": f"معرفة الحروف هي الخطوة الأولى في تعلم القراءة والكتابة لـ {user_name}.",
        "الحيوانات": f"التعرف على الحيوانات يعزز فهم {user_name} للتنوع البيئي.",
        "النباتات": f"تعلم عن النباتات يشجع {user_name} على حب الطبيعة واحترام البيئة.",
        "الفضاء": f"الفضاء يفتح آفاقاً واسعة لخيال {user_name} ويساعد على فهم الكون.",
    }

    # Generate focus based on input topic
    for topic, description in topics.items():
        if topic in user_input:
            prompt += f"يجب أن تركز القصة على {description}. "
            prompt += f"أيضًا، تذكر: {educational_messages[topic]}"
            motivational_message = educational_messages[topic]
            break
    else:
        motivational_message = f"التعلم يفتح آفاقًا جديدة ويزيد من معرفة {user_name}. استمر في استكشاف العالم من حولك، فكل يوم مليء بفرص التعلم الممتعة!"


    # Customize story based on age
    if 3 <= user_age <= 5:
        prompt += "يجب أن تكون القصة بسيطة ومفهومة، مع صور ذهنية تساعد الأطفال في التعلم. "
    elif 6 <= user_age <= 7:
        prompt += "القصة يمكن أن تكون أكثر تفصيلاً مع أمثلة توضيحية عن الموضوع. "
    elif 8 <= user_age <= 10:
        prompt += "يجب أن تتناول القصة الموضوع بشكل أكثر تعمقاً وتفصيلاً، مع تقديم معلومات جديدة للأطفال. "
    elif 11 <= user_age <= 12:
        prompt += "القصة يجب أن تقدم موضوعات معقدة بطريقة بسيطة ومشوقة مع تفاصيل أكثر علمية. "

    # Fixed elements for all stories
    prompt += "نهاية القصة يجب أن تكون سعيدة. "
    prompt += "عدد الشخصيات في القصة يجب أن يكون 2. "
    prompt += "موضوع القصة هو التعلم والتعليم. "
    prompt += "يجب أن تحتوي القصة على شعور بالحماس. "
    prompt += "القصة يجب أن تكون باللغة العربية الفصحى ومفهومة للأطفال. "
    prompt += "أكتب القصة مباشرة."

    # Output structure
    output = {
        "user_name": user_name,
        "story_type": story_type,
        "user_age": user_age,
        "story_content": prompt,
        "motivational_message": motivational_message,
        "note": "القصة مكتوبة بلغة بسيطة تناسب الأطفال."
    }

    return json.dumps(output, ensure_ascii=False, indent=4)


#قصص واقعية.



def complete_user_prompt_realistic_stories(user_prompt, user_age, template_parameters, user_name, feature_probability=0.15):
    # Define story type
    story_type = "قصص واقعية. "
    prompt = story_type
    prompt += f"{user_prompt}\n"

    # Determine the age group based on the input age
    age_group = get_age_group(user_age)
    if age_group != 'غير محددة':
        prompt += f"القصة موجهة للأطفال بعمر {age_group}. "
    else:
        prompt += f"العمر المدخل {user_age} خارج النطاق المخصص للقصة."

    # Add optional story features
    if 'place' in template_parameters and random.random() < feature_probability:
        prompt += f"تجري أحداث القصة في {random.choice(template_parameters['place'])}. "
    if 'ending' in template_parameters:
        prompt += f"نهاية القصة يجب أن تكون {random.choice(template_parameters['ending'])}. "
    if 'dialogue' in template_parameters and random.random() < feature_probability:
        prompt += f"تتضمن القصة {template_parameters['dialogue']}. "
    if 'num_of_characters' in template_parameters:
        prompt += f"عدد الشخصيات في القصة يجب أن يكون {random.choice(template_parameters['num_of_characters'])}. "
    if 'profession' in template_parameters and random.random() < feature_probability:
        prompt += f"أحد الشخصيات يعمل كـ{random.choice(template_parameters['profession'])}. "
    elif 'activity' in template_parameters and random.random() < feature_probability:
        prompt += f"يجب أن تتضمن القصة النشاط التالي: {random.choice(template_parameters['activity'])}. "
    if 'season' in template_parameters and random.random() < feature_probability:
        prompt += f"الأحداث تدور في فصل {random.choice(template_parameters['season'])}. "
    if 'emotion' in template_parameters and random.random() < feature_probability:
        prompt += f"تتضمن القصة شعورًا ب{random.choice(template_parameters['emotion'])}. "
    if 'moral' in template_parameters and random.random() < feature_probability:
        prompt += f"في نهاية القصة، يجب أن يتعلم البطل درسًا حول {random.choice(template_parameters['moral'])}. "

    prompt += "\nالقصة يجب أن تكون باللغة العربية الفصحى وموجهة للأطفال."

    # Motivational message
    motivational_message = f"تذكر يا {user_name} أن الحياة مليئة بالدروس القيمة. تعلم أن تكون صادقًا، متعاونًا، وتفكر بإيجابية."

    # Create output structure
    output = {
        "user_name": user_name,
        "story_type": story_type,
        "user_age": user_age,
        "story_content": prompt,
        "motivational_message": motivational_message,
        "note": "القصة مكتوبة بلغة بسيطة تناسب الأطفال."
    }

    return json.dumps(output, ensure_ascii=False, indent=4)

# Template parameters for realistic story elements
template_params_realistic = {
    'place': [
        "المدرسة", "الحديقة", "الملعب", "البيت", "المزرعة", "الشاطئ", "مركز التسوق", "مدينة صغيرة", "القرية"
    ],
    'ending': ['سعيدة', 'حزينة', 'ملهمة', 'تعليمية'],
    'dialogue': 'حوار بين شخصيتين في موقف يومي',
    'num_of_characters': [1, 2, 3, 4],
    'profession': ['طبيب', 'معلم', 'مهندس', 'مزارع', 'شرطي'],
    'activity': ['اللعب مع الأصدقاء', 'مساعدة الوالدين', 'المشاركة في مسابقة', 'زيارة الجد والجدة'],
    'season': ['الصيف', 'الشتاء', 'الربيع', 'الخريف'],
    'emotion': ['السعادة', 'الحزن', 'الخوف', 'الفرح'],
    'moral': ['أهمية الصداقة', 'التعاون والعمل الجماعي', 'الأمانة', 'التفكير الإيجابي']
}


#قصص حضارة وتراث السعوديه.
import random
import json


def generate_saudi_heritage_story_prompt(user_prompt, user_name, user_age, template_parameters):
    story_type = "قصص حضارة وتراث السعوديه"
    story_content = story_type
    story_content += f"{user_prompt}\n"
    age_group = get_age_group(user_age)
    mentioned_figure = None
    modern_projects = ["نيوم", "القدية", "رؤية 2030"]


    if any(project in user_prompt for project in modern_projects):

        story_type = "قصة حول إنجازات المملكة الحديثة."
        story_content = f"تتحدث القصة عن إحدى الإنجازات الحديثة مثل مشروع {random.choice(modern_projects)}، الذي يعكس رؤية المملكة الطموحة للمستقبل."
    else:

        if "ولي العهد" in user_prompt or "الأمير محمد بن سلمان" in user_prompt or "الامير محمد بن سلمان" in user_prompt:
            mentioned_figure = "ولي العهد محمد بن سلمان"
        else:

            for full_name in template_parameters['saudi_figure']:
                name_keywords = full_name.split()
                if all(keyword in user_prompt for keyword in name_keywords[:2]):
                    mentioned_figure = full_name
                    break


        if "أمير" in user_prompt and not mentioned_figure:

            kings_only = [king for king in template_parameters['saudi_figure'] if "ملك" in king]
            mentioned_figure = random.choice(kings_only)


        king_events = {
            "الملك عبدالعزيز بن عبدالرحمن آل سعود": [
                "توحيد المملكة العربية السعودية في 1932.",
                "معركة الرياض في 1902.",
                "استعادة الحجاز في 1925.",
                "اكتشاف النفط في 1938.",
                "إنشاء الوزارات والمؤسسات الحكومية."
            ],
            "الملك سعود بن عبدالعزيز آل سعود": [
                "توسعة الحرمين الشريفين.",
                "إنشاء جامعة الملك سعود.",
                "تطوير البنية التحتية.",
                "إنشاء مساكن شعبية.",
                "تعزيز العلاقات الخارجية."
            ],
            "الملك فيصل بن عبدالعزيز آل سعود": [
                "حظر النفط في 1973.",
                "دعم القضية الفلسطينية.",
                "توسيع العلاقات الدولية.",
                "تطوير التعليم.",
                "تأسيس منظمة التعاون الإسلامي."
            ],
            "الملك خالد بن عبدالعزيز آل سعود": [
                "ازدهار اقتصادي نتيجة ارتفاع أسعار النفط.",
                "توسعة الحرمين الشريفين.",
                "إنشاء الهيئة الملكية للجبيل وينبع.",
                "تطوير الرعاية الصحية.",
                "بناء الجامعات والمدارس."
            ],
            "الملك فهد بن عبدالعزيز آل سعود": [
                "تحرير الكويت في 1991.",
                "إصدار النظام الأساسي للحكم في 1992.",
                "تأسيس مجلس الشورى.",
                "إنشاء المدن الاقتصادية.",
                "تطوير البنية التحتية."
            ],
            "الملك عبدالله بن عبدالعزيز آل سعود": [
                "إطلاق برنامج الابتعاث الخارجي.",
                "توسعة الحرمين الشريفين.",
                "تأسيس جامعة الملك عبدالله للعلوم والتقنية.",
                "تطوير الرعاية الصحية والتعليم."
            ],
            "الملك سلمان بن عبدالعزيز آل سعود": [
                "إطلاق رؤية 2030.",
                "تمكين المرأة.",
                "الإصلاحات الاقتصادية والاجتماعية.",
                "مشاريع ضخمة مثل نيوم والقدية."
            ],
            "ولي العهد محمد بن سلمان": [
                "قيادة رؤية 2030.",
                "مشروع نيوم.",
                "الإصلاحات الاجتماعية.",
                "توسع صندوق الاستثمارات العامة.",
                "حملة مكافحة الفساد."
            ]
        }


    modern_projects = ["نيوم", "القدية", "رؤية 2030"]
    heritage_keywords = ["تراث السعودية", "آثار تراثية", "تراث سعودي", "التاريخ السعودي"]


    if any(project in user_prompt for project in modern_projects):

        story_type = "قصة حول إنجازات المملكة الحديثة."
        story_content = f"تتحدث القصة عن إحدى الإنجازات الحديثة مثل مشروع {user_prompt}، الذي يعكس رؤية المملكة الطموحة للمستقبل."

    elif any(keyword in user_prompt for keyword in heritage_keywords):
        story_type = "قصة حول تراث السعودية."
        story_content = f"تتناول القصة جوانب من {user_prompt}، مثل التراث المعماري، والحرف التقليدية، والمواقع التاريخية التي تروي قصص الأجداد وإسهاماتهم."


    else:

        if "ولي العهد" in user_prompt or "الأمير محمد بن سلمان" in user_prompt:
            mentioned_figure = "ولي العهد محمد بن سلمان"
        else:

            for full_name in template_parameters['saudi_figure']:
                name_keywords = full_name.split()
                if all(keyword in user_prompt for keyword in name_keywords[:2]):
                    mentioned_figure = full_name
                    break


        story_content = user_prompt if not mentioned_figure else ""


    if mentioned_figure:
        story_content = f"تتحدث القصة عن {mentioned_figure} وواقعة تاريخية هامة. "
        random_event = random.choice(king_events[mentioned_figure])
        story_content += f"تتناول القصة {random_event}"



    motivational_message = f"تذكر يا {user_name}، أن المملكة مليئة بالتاريخ الغني والتقاليد العريقة، وقصصها هي مصدر فخر لكل مواطن. المستقبل بين يديك وأنت قادر على أن تكون جزءًا من هذه الإنجازات العظيمة."


    output = {
        "user_name": user_name,
        "story_type": story_type,
        "user_age": age_group,
        "story_content": story_content,
        "motivational_message": motivational_message,
        "note": "القصة مكتوبة بلغة بسيطة تناسب الأطفال."
    }

    return output

template_params_saudi_heritage = {
    'age': ['3-5', '5-8', '8-10', '10-12'],
    'saudi_figure': [
        "الملك عبدالعزيز بن عبدالرحمن آل سعود",
        "الملك سعود بن عبدالعزيز آل سعود",
        "الملك فيصل بن عبدالعزيز آل سعود",
        "الملك خالد بن عبدالعزيز آل سعود",
        "الملك فهد بن عبدالعزيز آل سعود",
        "الملك عبدالله بن عبدالعزيز آل سعود",
        "الملك سلمان بن عبدالعزيز آل سعود",
        "ولي العهد محمد بن سلمان"
    ]
}

def generate_story_based_on_choice(type,subType,story,name,age):
    if(type=="إسلامية"):
        prompt=complete_user_prompt_islamic_stories(template_params_islamic,subType,story,name,age)
        return prompt
    elif(type=="تعليمية"):
        prompt=complete_user_prompt_educational_stories(story,age,name)
        return prompt
    elif(type=="خيالية"):
        prompt=complete_user_prompt_Imaginary_stories(story,age,template_params,name)
    elif(type=="واقعية"):
        prompt=complete_user_prompt_realistic_stories(story,age,template_params_realistic,name)
    elif(type=="حضارة وتراث السعوديه"):
        prompt=generate_saudi_heritage_story_prompt(story,name,age,template_params_saudi_heritage)
    





