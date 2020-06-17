from emailtemplates import add_or_update_template

mp_police = {
    "subject": "Suspension of Exportation of Policing Equipment to the US",
    "body": """
Dear {t[name]},


My name is {u[name]} and I am a resident of {t[constituency]}, at {u[address]}.

I am writing to you today to implore you to put pressure on the government to stop the exportation of tear gas, rubber bullets and riot shields to the United States and to condemn Trump's use of force against his own citizens.
After the shocking footage of the police and the national guard using excessive force against Black Lives Matter protesters across the United States, the UK should immediately stop all policing and security equipment export to the US where there is a clear risk of further misuse. This is something the UK is obligated to do under its own laws.
Given the evidence emerging from multiple US cities, there is a very real risk of UK-manufactured tear gas or rubber bullets being used against George Floyd protesters in dangerous and highly inappropriate ways - ministers must respond to this.
Ministers should be making detailed case by case assessments of any requests for equipment from individual US police forces – withholding exports from any that have clearly acted irresponsible during the current crisis. The UK has an obscene track record of looking the other way when UK arms and security equipment is misused overseas. Now is the time to change that.
In addition to immediate suspension of UK sales of tear gas, riot shields and rubber bullets to the US, the UK Government should condemn Trump's use of force against his own citizens. The behaviour he has exhibited is anti-democratic and cruel. It sets a dangerous precedent and the UK government must acknowledge this.
In short, my requests to you are:


    - Immediate stopping of UK sales of teargas, riot shield and rubber bullets to the US
    - Condemnation of Trump's use of force against his own citizens


Thank you for your time. Please respond to this email as soon as you see fit.
Regards,

{u[name]}
    """,
    "name": "Suspend Police Equipment Exports",
    "topics": ["black-lives-matter"],
    "public": True,
}


# IMPORTANT: Gavin Williamson template removed until we can find a way to contanct him via his preferred method for enquiries about educations


gavinwilliamson_email = {
    "name": "National Curriculum Change",
    "topics": ["black-lives-matter"],
    "subject": "Make Black histories mandatory in the national curriculum",
    "body": """
Dear {t[name]},


As supporters of The Black Curriculum, we are dismayed by the events of the last few weeks which have disproportionately affected Black people in the UK - exacerbated by Covid19, and the subsequent lack of response by those in authority. Thousands of us, the British voting public are grief stricken and concerned about the existing status-quo in the UK, which disregards the lives and contributions of Black British people. We would like to bring to your attention some of the structural inequalities in the UK, especially pertaining to education and the national curriculum.
As you are aware, the national curriculum excludes Black histories throughout, and omits the vast contributions Black people have made to the UK. As a result, young people who learn from the national curriculum are not given a full or accurate version of British history, which limits their opportunities and futures in an increasingly diverse landscape. Despite numerous calls over the years to reform the national curriculum to incorporate Black histories, these requests have been denied. Learning Black history should not be a choice but should be mandatory. Our curriculum should not be reinforcing the message that a sizeable part of the British population are not valued.
Black people have been in Britain since Roman times, have contributed to and shaped the foundation of our society. Therefore, we are asking you to specifically include Black histories on the national curriculum from KS1 - KS4 to include Black British histories across different subject areas, including History, Citizenship, English and PSHE. By doing so, you can invest in the lives and opportunities of all young people across the UK to become fully rounded citizens and create a better, fairer society. This is in line with the DfE Strategy’s first principle as highlighted in 2015-2020 World-class Education and Care: “Our first principle is to ensure each policy puts children and young people first. We must not let anything detract from improving the lives and opportunities of those who rely on the education and children social care systems.” – p.11, DfE strategy 2015-2020

The Black Curriculum is demanding that you work with them to adequately incorporate Black British history into the national curriculum and to fulfil your goals of British education truly being able to help the government’s “commitments to social justice and economic growth.”
Will you meet with the leaders of the Black Curriculum? They are ready and waiting for your response.

With thanks,

{u[name]}""",
}
gavinwilliamson_email["target"] = {
    "name": "Secretary of State for Education",
    "email": "gavin.williamson.mp@parliament.uk",
}

belly_mujinga_mp = {
    "name": "Belly Mujinga - MP",
    "subject": "Justice for Belly Mujinga",
    "author_url": "https://docs.google.com/document/d/1P7owSv_blKdVaAzII-ySKpk1Vo7w2c_mpE4wUSmRPBQ/edit#heading=h.xvqvign7bp33",
    "body": """
Dear {t[name]},

My name is {u[name]} and I am a resident of {t[constituency]}, at {u[address]}.

I write further to my previous email regarding Black Lives Matter with a specific demand for justice for Belly Mujinga, a railway ticket office worker who contracted COVID-19 and subsequently died. I am sure you are aware that Mujinga, a key worker, was spat on by a member of the public claiming he was infectious on March 21.

Despite this event taking place, a spokesperson for British Transport Police has recently stated that they will take no further action into the case, given that the “tragic death of Belly Mujinga was not a consequence of this incident.”

However, in Glasgow, a man who spat at a police officer and joked about coronavirus has been jailed for twelve months.

I recognise that there may be legal differences between each of the four nations, but it is unconscionable to me that there is such a gulf between the consequences of these two actions. Regardless of whether illness may or may not be attributed to the assault, it is an assault nonetheless, and an assault that in the case of Belly Mujinga has not been given due weight.

I find this especially troubling following the report published into disproportionate BAME deaths due to COVID-19, and ask whether Belly Mujinga - a Congolese woman with underlying health issues, who was reportedly scared for her life - was a victim of a poor response to the coronavirus pandemic on the part of British authorities.

I urge the UK government to seek to reopen the investigation into the assault on Belly Mujinga.

Yours sincerely,

{u[name]}""",
    "public": True,
}


belly_mujinga_govia = {
    "name": "Belly Mujinga - Govia",
    "topics": ["black-lives-matter"],
    "subject": "Justice for Belly Mujinga",
    "body": """
Dear {t[name]},

I am writing to you in regards to the recent death of Belly Mujinga, who worked for Govia Thameslink Railway. Her death follows after an assault was carried out on 21st March in which her and colleagues were spat at and coughed on during their shift at London Victoria Station.

As I am sure you are aware, it was revealed on 29th May that The British Transport Police ruled that they believed there was no link between the act of assault and her death and stated that ‘no further action will be taken’, closing the case. In spite of this Ms. Mujinga’s passing on 5th April comes just two weeks after the assault had taken place and after several days having been admitted to hospital and testing positive for COVID-19.

Following the outcome in regards to Ms. Mujinga’s death and The British Transport Police’s dismissal of the case, I urge you as CEO of Govia Thameslink Railway, to take action on her behalf and to that of her loved ones following her death. As an essential worker, Ms. Mujinga was failed by the Govia Thameslink Rail to be protected after she had expressed concerns for her wellbeing due to respiratory issues. Ms. Mujinga made appeals to work away from crowds at the busy station due to there being no PPE provided for railway workers, her concerns were inadequately dismissed.

In spite of the assault carried out and Ms. Mujinga’s passing it was reported by The Independent in an article released on 14th May by a worker at London Victoria station that “There’s not much being done to check all the staff, today is the first day we have had masks.” Going forward, it shows that you have not prioritised the protection and the safety of your staff to prevent such an act happening again in the future.

So I ask, why did you ignore Belly’s requests to work away from crowds during the pandemic as she had underlying health issues?

Further, why did it take weeks for Govia to surrender the CCTV footage to the police?

As a concerned individual I urge you to recognise the needs of more effective regulations and protection of railway workers at Govia Thameslink Rail during this time and for an assault similar to that of Ms Mujinga which effectively cost her life does not take place again.

Until responsible actions are taken to honour the death of Belly and prevent the future assault of your workers and you take full responsibility for your role in Belly's murder, I have decided to boycott Southern Rail, Gatwick Express, Great Northern and Thameslink.

Regards,

{u[name]}""",
    "public": True,
}
belly_mujinga_govia["target"] = {
    "name": "Patrick Verwer",
    "email": "Patrick.Verwer@gtrailway.com",
}


shukri_abdi = {
    "name": "Justice for Shukri Abdi",
    "topics": ["black-lives-matter"],
    "subject": "Justice For Shukri Abdi",
    "body": """
Dear {t[name]},

As your constituent, I am writing to call upon you to take action against Hazel Wood High School for concerning patterns of failures to protect both staff and pupils from bullying, resulting in deaths; and Greater Manchester Police for failing to properly investigate the murder of Shukri Abdi due to institutionalised racism. We demand justice for Shukri Abdi.

The body of Shukri, who first came to the UK in January 2017 as a refugee seeking a better life, was found in the River Irwell in Bury, Greater Manchester in June 2019. An inquest heard that Shukri had been threatened by her class peer/s and told: “if you don’t get into the water, I’m going to kill you”. I am utterly beyond outraged, saddened and disappointed that children in our society can be so badly let down and failed. Shukri has been described as an “angelic, funny and kind-hearted little girl” that had much to offer.

There are very concerning patterns of failure to meet adequate safeguarding measures at Hazel Wood High School, who has since rebranded from Broad Oak Sports College. The latest Ofsted report concluded that the school was “inadequate” and has thus since been put on “special measures” by Her Majesty’s Chief Inspector, per section 44(1) of the Education Act 2005. Shurki has been woefully failed by Hazel Wood High School. Their incompetence can be argued to have played a key role in the murder of Shukri. Additionally, Manchester Evening News reported that in 2015 a “senior teacher, Caroline Bailey, at Broad Oak Sports College” (Hazel Wood High School) had committed suicide; an inquest heard that this was, yet again, due to “strategic bullying” from co-workers within the school. I urge you to raise these concerning patterns of failure to safeguard against bullying, resulting in deaths, at Hazel Wood High School, with the Secretary of State for Education, Gavin Williamson.

Furthermore, Greater Manchester Police (GMP) must also be investigated for their ineptitude in investigating this murder, no less a sign of institutionalised racism that has failed yet another black life. Reports show that the Officers at the scene of the murder took witness statements from only two out of four present at Shukri’s death. Her murder was ruled by GMP to be an accident within two weeks. One can argue that Shukri’s murder has not been properly investigated due to her ethnic background and, therefore, has led to my loss of confidence in the impartiality of the GMP in serving to protect and uphold justice for all citizens. I urge you to raise these concerns with the Mayor of Manchester, Andy Burnham.

Moreover, Shukri’s death can also be placed in a wider landscape of institutional racism within modern-day Britain. Yvette Cooper, Labour MP and chair of the home affairs select committee damned the “deeply unfair shambles” of how asylum seekers are accommodated. The Guardian analysis of Home Office data found that “more than half of all asylum seekers (57%) housed by the government are done so in the poorest third of the country”. I trust that we can agree that we must do more to support the most vulnerable in our society and that these statistics are wholly unacceptable.

As you are well aware of the global outrage against injustices rooted in systemic and perpetual institutionalised racism, I leave you with the words of human rights activist and organiser of the protests demanding justice for Shukri Abdi, Bashir Ibrahim: “she was failed when she was alive and she’s still being failed now as she’s dead”.

I look forward to your urgent response,

Yours sincerely,

{u[name]}
""",
    "public": True,
}

# Gender Recognition Act Templates

vanity_project_gra = {
    "name": "Vanity Project GRA Template",
    "topics": ["gender-reform-act"],
    "subject": "Gender Reform Act Withdrawal",
    "author_url": "https://www.facebook.com/story.php?story_fbid=2799692286983914&id=1701399066813247",
    "more_info_url": "https://www.stonewall.org.uk/truth-about-trans#trans-people-britain",
    "body": """
Dear {t[name]},

I hope you’re well. As one of your constituents, I am writing to ask that you stand against plans to scrap reform of of the Gender Recognition Act and protect the rights of transgender women and nonbinary people to use female public toilets and women’s refuges’.

I was horrified to read about this planned legislation in the news (please see article linked here: https://www.theguardian.com/uk-news/2020/jun/14/trans-rights-government-reported-to-be-dropping-gender-self-identifying-plans). This terrifying step backwards in the progress of basic human rights for transgender people pupports to be in favour of protecting cisgender women’s safety. However, there is absolutely no evidence that this legislation will do this and, in most cases, this is being used in order disguise pure bigotry against transgender people.

One of the main arguments used against allowing transgender people the right to self identify as their gender is that it will increase violence towards cisgender women from men. The logic is that it will allow violent and abusive men to ‘self identify’ as women, purely in order to gain access to safe female spaces, such as public toilets and women’s refuge centres.

However, I have not been able to find a single piece of evidence that this has been the case in any areas where trans women are allowed to self identify. In a 2018 Stonewall report (link: https://www.stonewall.org.uk/system/files/stonewall_and_nfpsynergy_report.pdf), after extensive interviews with domestic and sexual abuse support services in the UK, it was found that there was ‘a clear consensus
that services’ thorough risk assessment procedures would safeguard against this. These
participants said that gender recognition reform would not compromise their ability to protect
their service against, or turn away, any abusive or disruptive individual.’

At the same time, scrapping reform of the gender recognition act and banning transgender women from using women’s bathrooms and domestic abuse refuge centres, will cause immense harm to the transgender community.

Firstly, transgender people having to go through long, complicated and often expensive processes with medical professionals in order to have their gender legally recognised is extremely destructive to their mental health. One study found transgender people are almost ten times as likely to commit suicide as cisgender people.

Secondly, not allowing transgender women to access safe spaces for women will cause an increase in violence towards transgender women. Domestic abuse towards trans women is extremely common. This report (https://www.scottishtrans.org/wp-content/uploads/2013/03/trans_domestic_abuse.pdf) found that 80% of the transgender women they surveyed had experienced emotionally, sexually, or physically abusive behaviour by a partner or ex-partner. Public bathrooms are also a common site for abuse and hate crimes towards transgender women.

To put it bluntly, people will die because of this legislation. They will kill themselves and they will be beaten to death.

The transgender community is small and disempowered. Trans people face high rates of unemployment and incarceration all over the world. Depression is rife in the community and many avoid public life all together for threat of violence and exclusion. There are no transgender MPs in the UK.

I urge you to stand up for the rights of transgender people in parliment. They desperately need allies, now more than ever.

Thank you and I hope to hear from you soon.

All the best,

Yours sincerely,

{u[name]}
{u[address]}
""",
    "public": False,
}

gra_mp_from_trans_person = {
    "name": "GRA Template From Trans Person",
    "topics": ["gender-reform-act"],
    "subject": "Gender Reform Act Withdrawal",
    "author_url": "https://docs.google.com/document/d/1j0FdGD2CY_nsxqbzLRBLLRTgtm8trlYZ7nUuVN9mBHE/edit",
    "more_info_url": "https://gra.good.do/trusstme/trusstme/",
    "body": """
Dear {t[name]},

I'm writing to you as a resident of {t[constituency]} and trans person who is frightened by the proposed rollbacks to safeguards for trans dignity and safety in this country. I'm frightened for myself, as I know my own existence will become harder. I'm frightened for my trans siblings across the UK, especially the most vulnerable members of our community, the black trans women who already live in fear for their lives, suffering at the nexus of every oppressive system that exists. I'm frightened for intersex people, who are already medicalised against their wills, often subject to non-consensual surgeries, and whom the UK's existing binary forms of gender recognition erase entirely. I'm even frightened for cisgender people (non-trans people): legislation that punishes gender non-conformity and polices bodies and behaviour according to gender is bad for everyone, invasive for everyone and will further entrench gender inequality.

The plans leaked on the front page of the Sunday Times on 14th June 2020 represent the biggest threat to LGBT+ rights in the UK since Section 28. The plans include abandoning progressive reforms to the Gender Recognition Act, and intensifying through law the exclusion of trans people from single sex spaces. If you proceed with these plans, you will be responsible for the most serious legislative regression in LGBT+ rights in the UK for decades. History will not look kindly on you.

The leaked plans indicate the government will scrap plans to allow people to self-identify their gender (i.e. those who want legal recognition will still be gatekept by the medical community) despite 70% of respondents to the GRA consultation being in favour of self-identification. The Sunday Times states that “officials believe the results were skewed by an avalanche of responses generated by trans rights groups.” However, it is extremely reasonable that trans people should have a say in legislation the outcome of which will affect them profoundly and daily. This dismissal of the results also overlooks the fact that anti-trans groups were campaigning equally hard to collect responses to the consultation which were antagonistic to trans rights; yet, despite a large, active and hostile campaign to skew the results against progressive reform, an overwhelming majority of respondents still favoured self-identification. To dismiss this result is deeply undemocratic. As you are aware, people are angry right now with the government on many fronts: to demonstrate so clearly to an angry populace that engaging in "democratic" systems will do nothing to further the liberation of the most marginalised would be a very bad move on your part right now.

The scrapping of GRA reform, redoubling of medical gatekeeping, and policing of single sex spaces threaten the dignity, safety and lives of your trans citizens. Those who support these outcomes wish to see us written out of existence. If you proceed on your current course, you will be authorising further violence towards any transgender person and indeed any visibly non-conforming person. The state will embolden those who continually call into question our bodies and experiences, attempt to exclude us from vital and potentially lifesaving services, and even perpetrate physical violence against our most vulnerable. This is an issue of race and class. The people who will be most impacted are those who are already marginalised on the basis of race, and who know from experience that their lives are not valued by the establishment. Those who lack the material resources to protect themselves from the dangers they face daily simply for trying to exist. Those for whom expensive medical transition is an impossibility. Those who will never fit white, western, ablist, sexist, and cissexist ideals of what a man or a woman should be. Those who wish actively to reject gendered systems of oppression, and who are punished for acting out. Make no mistake, the current plans are not only transphobic, they are racist, classist, ablist, misogynistic, and will entrench and intensify existing inequalities. You must abandon them.

Trans people are not a threat to anyone's safety. Trans people simply want to exist in safety and peace. Trans people are in overwhelming numbers the victims of violence, not its perpetrators. I urge you not to further exclude and marginalise trans people in all areas of public life and further compromise the UK's human rights record. If you proceed with your plans, you will make yourself complicit with discrimination, harassment, violence, murder, and the subtler but no less deadly systems which oppress trans people worldwide.


Yours sincerely,

{u[name]}
{u[address]}
""",
    "public": False,
}

gra_mp_from_cisgender_person = {
    "name": "GRA Template From Cisgender Person",
    "topics": ["gender-reform-act"],
    "subject": "Gender Reform Act Withdrawal",
    "author_url": "https://docs.google.com/document/d/1xjgLryhWABGtQK0kR8zYFymMxQOoueqc3sohPJPfis8/edit",
    "more_info_url": "https://gra.good.do/trusstme/trusstme/",
    "body": """
Dear {t[name]},

I’m writing to you as a resident of {t[constituency]} about the recent news, as covered in the Sunday Times, about potential government plans to scrap GRA reform, restrict the use of single sex spaces, and reduce access to affirming and potentially life-saving medical transition. As an ally to the trans community, I am opposed to all of these. Introducing this legislation would make me fear not only for my trans siblings, but also for any gender non-conforming person who’s appearance may be brought under public scrutiny when they simply want to go swimming, or use a public toilet.

Firstly, addressing the plans to scrap GRA reform. The reform would have allowed trans people to obtain a Gender Recognition Certificate (GRC) through self-identification. This reform would make the process of changing one’s birth certificate much easier. Currently the process of obtaining a GRC is long and can be difficult. Many trans people currently don’t opt for a GRC because the process is off-putting for them. 70% of respondents to the GRA reform survey supported the change to self-identification. The idea that the result was somehow improperly swayed by trans activists is questionable at best. Trans people deserve to have a say in their own rights, and many trans people attest to the fact that the loudest and most vocal campaigns to fill out the survey generally came from those opposing the measure. 70% is a much higher majority than other public consultations have taken as informative.

Secondly, restricting the use of single sex spaces. Trans women have been using women’s spaces for decades with no issues arising. Forcing them to use men’s spaces is just as dangerous for their safety as forcing a cisgender woman to do the same, if not more so, from the intersections of misogyny and transphobia that cause trans women to experience disproportionate levels of violence in society. But trans people won’t even be the only ones impacted. Gender non-conforming individuals such as butch lesbians have also experienced harassment when trying to use women’s toilets before, and bringing forth legislation such as what has been proposed, will surely only encourage such invasive questioning and harassment to become more prevalent.

Finally addressing the issue of medical transition and access to trans healthcare. Trans people already face multi-year wait times for treatment through the NHS, and private options aren’t financially possible for many. It’s currently unclear as to what measures will be taken to make access to medical transition more strictly regulated. However, I am opposed to making healthcare any more difficult to access than it currently is, and would be in favour of improving access if possible. Medical transition can be life-saving for trans people with severe dysphoria. Furthermore, there is already a lot of misinformation from those who oppose gender-affirming treatment spreading about how trans people are treated at Gender Clinics. For example many are claiming hormones and surgeries are being given to primary aged children, which is categorically untrue. I worry that restricting access to gender-affirming care will give further fire to these claims, on top of all the materially negative impacts on the lives on trans and non-binary people.

I would like to thank you for taking the time to read this email. As your constituent, I urge you to do the following:

Back a reform of the GRA in line with what 70% of respondents to the government survey supported
Support the rights of trans people to access the single sex spaces that best fit their gender identity, and oppose legislation to restrict this
Oppose restriction of access to gender-affirming medical care for trans people

You could also consider calling for government action that improves the wait time for access to healthcare for trans people, and legislation that recognises the existence of non-binary individuals, who currently have no suitable gender marker for their official documentation.

Thank you for your time, and I look forward to receiving your response,

{u[name]}
{u[address]}
""",
    "public": False,
}


for t in [
    mp_police,
    gavinwilliamson_email,
    belly_mujinga_mp,
    belly_mujinga_govia,
    shukri_abdi,
    vanity_project_gra,
    gra_mp_from_trans_person,
    gra_mp_from_cisgender_person,
]:
    print("Adding/updating: {}".format(t["name"]))
    add_or_update_template(**t)
