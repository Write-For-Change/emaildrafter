"""
Template for the emails the app should send.
ToDo:
    1. Change Filling function to generic dictionary filler. (Completed)
    2. Edit the functions that use the returned email templates to get information correctly (i.e. e.subject is fine, but now target email is e.target["email"]) (completed)
    3. Gather all email templates automatically
    4. Store them in a file
    5. Allow people to submit template ideas
"""
from copy import deepcopy


class EmailTemplate:
    """Store an unfilled email template, implement a filling function (which can be extended later)"""

    def __init__(self, subject, body, target=None, cc=None):
        self.subject = subject
        self.body = body
        self.target = None
        self.cc = cc
        self.filled = False

    def __str__(self):
        return str([self.subject, self.body])

    def set_target(self, name, email, constituency=None, address=None):
        if not address:
            address = "[ENTER YOUR ADDRESS HERE]"
        self.target = {
            "name": name,
            "email": email,
            "constituency": constituency,
            "address": address,
        }

    def fill(self, user_info):
        """Fill an unfilled body with provided user information (user_info)"""
        if self.filled:
            # Already filled, so do not need to fill again
            return self.filled
        if self.target is None:
            # Target not set, so cannot fill
            self.filled = False
            return self.filled
        self.body = self.body.format(t=self.target, u=user_info)
        self.filled = True
        return self.filled


# For Reference this is what I would expect our information about the user and target to look like
user_info = {"name": "John Smith", "postcode": "AB1 2CD"}
target_info = {
    "name": "Big Bad Government",
    "constituency": "Westminster",
    "email": "bigbadboi@hotmail.co.uk",
}

mp_police = EmailTemplate(
    subject="Suspension of Exportation of Policing Equipment to the US",
    body="""
Dear {t[name]},


My name is {u[name]} and I am a resident of {t[constituency]} constituency, at {u[address]}.

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
)


gavinwilliamson_email = EmailTemplate(
    subject="Make Black histories mandatory in the national curriculum",
    body="""
Dear {t[name]},


As supporters of The Black Curriculum, we are dismayed by the events of the last few weeks which have disproportionately affected Black people in the UK - exacerbated by Covid19, and the subsequent lack of response by those in authority. Thousands of us, the British voting public are grief stricken and concerned about the existing status-quo in the UK, which disregards the lives and contributions of Black British people. We would like to bring to your attention some of the structural inequalities in the UK, especially pertaining to education and the national curriculum.
As you are aware, the national curriculum excludes Black histories throughout, and omits the vast contributions Black people have made to the UK. As a result, young people who learn from the national curriculum are not given a full or accurate version of British history, which limits their opportunities and futures in an increasingly diverse landscape. Despite numerous calls over the years to reform the national curriculum to incorporate Black histories, these requests have been denied. Learning Black history should not be a choice but should be mandatory. Our curriculum should not be reinforcing the message that a sizeable part of the British population are not valued.
Black people have been in Britain since Roman times, have contributed to and shaped the foundation of our society. Therefore, we are asking you to specifically include Black histories on the national curriculum from KS1 - KS4 to include Black British histories across different subject areas, including History, Citizenship, English and PSHE. By doing so, you can invest in the lives and opportunities of all young people across the UK to become fully rounded citizens and create a better, fairer society. This is in line with the DfE Strategy’s first principle as highlighted in 2015-2020 World-class Education and Care: “Our first principle is to ensure each policy puts children and young people first. We must not let anything detract from improving the lives and opportunities of those who rely on the education and children social care systems.” – p.11, DfE strategy 2015-2020

The Black Curriculum is demanding that you work with them to adequately incorporate Black British history into the national curriculum and to fulfil your goals of British education truly being able to help the government’s “commitments to social justice and economic growth.”
Will you meet with the leaders of the Black Curriculum? They are ready and waiting for your response.

With thanks,

{u[name]}
    """,
)
gavinwilliamson_email.set_target(
    name="Secretary of State for Education", email="gavin.williamson.mp@parliament.uk"
)

belly_mujinga_mp = EmailTemplate(
    subject="Justice for Belly Mujinga",
    body="""
Dear {t[name]},

My name is {u[name]} and I am a resident of {t[constituency]} constituency, at {u[address]}.

I write further to my previous email regarding Black Lives Matter with a specific demand for justice for Belly Mujinga, a railway ticket office worker who contracted COVID-19 and subsequently died. I am sure you are aware that Mujinga, a key worker, was spat on by a member of the public claiming he was infectious on March 21.

Despite this event taking place, a spokesperson for British Transport Police has recently stated that they will take no further action into the case, given that the “tragic death of Belly Mujinga was not a consequence of this incident.”

However, in Glasgow, a man who spat at a police officer and joked about coronavirus has been jailed for twelve months.

I recognise that there may be legal differences between each of the four nations, but it is unconscionable to me that there is such a gulf between the consequences of these two actions. Regardless of whether illness may or may not be attributed to the assault, it is an assault nonetheless, and an assault that in the case of Belly Mujinga has not been given due weight.

I find this especially troubling following the report published into disproportionate BAME deaths due to COVID-19, and ask whether Belly Mujinga - a Congolese woman with underlying health issues, who was reportedly scared for her life - was a victim of a poor response to the coronavirus pandemic on the part of British authorities.

I urge the UK government to seek to reopen the investigation into the assault on Belly Mujinga.

Yours sincerely,

{u[name]}
    """,
)

belly_mujinga_govia = EmailTemplate(
    subject="Justice for Belly Mujinga",
    body="""
Dear {t[name]},

I am writing to you in regards to the recent death of Belly Mujinga, who worked for Govia Thameslink Railway. Her death follows after an assault was carried out on 21st March in which her and colleagues were spat at and coughed on during their shift at London Victoria Station.

As I am sure you are aware, it was revealed on 29th May that The British Transport Police ruled that they believed there was no link between the act of assault and her death and stated that ‘no further action will be taken’, closing the case. In spite of this Ms. Mujinga’s passing on 5th April comes just two weeks after the assault had taken place and after several days having been admitted to hospital and testing positive for COVID-19.

Following the outcome in regards to Ms. Mujinga’s death and The British Transport Police’s dismissal of the case, I urge you as CEO of Govia Thameslink Railway, to take action on her behalf and to that of her loved ones following her death. As an essential worker, Ms. Mujinga was failed by the Govia Thameslink Rail to be protected after she had expressed concerns for her wellbeing due to respiratory issues. Ms. Mujinga made appeals to work away from crowds at the busy station due to there being no PPE provided for railway workers, her concerns were inadequately dismissed.

In spite of the assault carried out and Ms. Mujinga’s passing it was reported by The Independent in an article released on 14th May by a worker at London Victoria station that “There’s not much being done to check all the staff, today is the first day we have had masks.” Going forward, it shows that you have not prioritised the protection and the safety of your staff to prevent such an act happening again in the future.

So I ask, why did you ignore Belly’s requests to work away from crowds during the pandemic as she had underlaying health issues?

Further, why did it take weeks for Govia to surrender the CCTV footage to the police?

As a concerned individual I urge you to recognise the needs of more effective regulations and protection of railway workers at Govia Thameslink Rail during this time and for an assault similar to that of Ms Mujinga which effectively cost her life does not take place again.

Until responsible actions are taken to honour the death of Belly and prevent the future assault of your workers and you take full responsibility for your role in Belly's murder, I have decided to boycott Southern Rail, Gatwick Express, Great Northern and Thameslink.

Regards,

{u[name]}
    """,
)
belly_mujinga_govia.set_target(
    name="Patrick Verwer", email="Patrick.Verwer@gtrailway.com"
)

# Re: The murder of a 12-year-old schoolgirl, Shukri Yahya Abdi.
shukri_abdi = EmailTemplate(
    subject="Justice For Shukri Abdi",
    body="""
Dear {t[name]},

As your constituent living in {t[constituency]}, I am writing to call upon you to take action against Hazel Wood High School for concerning patterns of failures to protect both staff and pupils from bullying, resulting in deaths; and Greater Manchester Police for failing to properly investigate the murder of Shukri Abdi due to institutionalised racism. We demand justice for Shukri Abdi.

The body of Shukri, who first came to the UK in January 2017 as a refugee seeking a better life, was found in the River Irwell in Bury, Greater Manchester in June 2019. An inquest heard that Shukri had been threatened by her class peer/s and told: “if you don’t get into the water, I’m going to kill you”. I am utterly beyond outraged, saddened and disappointed that children in our society can be so badly let down and failed. Shukri has been described as an “angelic, funny and kind-hearted little girl” that had much to offer.

There are very concerning patterns of failure to meet adequate safeguarding measures at Hazel Wood High School, who has since rebranded from Broad Oak Sports College. The latest Ofsted report concluded that the school was “inadequate” and has thus since been put on “special measures” by Her Majesty’s Chief Inspector, per section 44(1) of the Education Act 2005. Shurki has been woefully failed by Hazel Wood High School. Their incompetence can be argued to have played a key role in the murder of Shukri. Additionally, Manchester Evening News reported that in 2015 a “senior teacher, Caroline Bailey, at Broad Oak Sports College” (Hazel Wood High School) had committed suicide; an inquest heard that this was, yet again, due to “strategic bullying” from co-workers within the school. I urge you to raise these concerning patterns of failure to safeguard against bullying, resulting in deaths, at Hazel Wood High School, with the Secretary of State for Education, Gavin Williamson.

Furthermore, Greater Manchester Police (GMP) must also be investigated for their ineptitude in investigating this murder, no less a sign of institutionalised racism that has failed yet another black life. Reports show that the Officers at the scene of the murder took witness statements from only two out of four present at Shukri’s death. Her murder was ruled by GMP to be an accident within two weeks. One can argue that Shukri’s murder has not been properly investigated due to her ethnic background and, therefore, has led to my loss of confidence in the impartiality of the GMP in serving to protect and uphold justice for all citizens. I urge you to raise these concerns with the Mayor of Manchester, Andy Burnham.

Moreover, Shukri’s death can also be placed in a wider landscape of institutional racism within modern-day Britain. Yvette Cooper, Labour MP and chair of the home affairs select committee damned the “deeply unfair shambles” of how asylum seekers are accommodated. The Guardian analysis of Home Office data found that “more than half of all asylum seekers (57%) housed by the government are done so in the poorest third of the country”. I trust that we can agree that we must do more to support the most vulnerable in our society and that these statistics are wholly unacceptable.

As you are well aware of the global outrage against injustices rooted in systemic and perpetual institutionalised racism, I leave you with the words of human rights activist and organiser of the protests demanding justice for Shukri Abdi, Bashir Ibrahim: “she was failed when she was alive and she’s still being failed now as she’s dead”.

I look forward to your urgent response,

Yours sincerely,

{u[name]}
{u[address]}
    """,
)

mp_solidarity = EmailTemplate(
    subject="Request for Solidarity",
    body="""
Dear {t[name]},  


My name is {u[name]} and I am one of your constituents, living at {u[address]}. I am writing to ask you to support your Black constituents and the Black community globally.

Matt Hancock on 2/6/2020 said that “Black Lives Matter” but we can only take this statement as lip service until the following actions take place. We need you to act as our advocate and:

1) Demand the immediate suspension of UK sales of teargas, rubber bullets, and riot shields to the US. This is to prevent the UK condoning the use of excessive and militarised force in policing Black people in the US.
2) Demand explicit condemnation of President Trump’s incitement of violence among US citizens and the police’s use of brutal force and physical violence against protesters.
3) Demand explicit condemnation of the UK police’s use of brutal force and physical violence against protesters.
4) Start an inquiry into why BAME people are disproportionately affected by the COVID-19 virus.
5) Demand justice for Belly Mujinga who was working on the front lines during this pandemic. She was assaulted by being spat at and coughed on. I would like you to demand an investigation into why Govia Thameslink did not provide Ms Mujinga with PPE despite their knowledge of her health conditions.

This is only a short list of possible actions you could take to protect and better the lives of the Black community, and sustained advocacy and active allyship is essential. This government’s continued complacency is violence and the endorsement of the oppression of Black people worldwide. History will look back at your actions during this time, just as we look to you now for leadership.

I would appreciate it if I received some form of response or acknowledgement to these concerns. Thank you in advance for your help with this matter and please keep me informed of any progress.

I look forward to hearing your response in due course.

Yours sincerely,

{u[name]}
    """,
)

mp_lgsmigrants = EmailTemplate(
    subject="Racial Inequality in the UK",
    body="""
Dear {t[name]},

I write to you as a resident of {t[constituency]} concerning state-sanctioned violence against Black people around the world, including here in the UK. This is not exclusively an American problem. The protests in the US in reaction to George Floyd’s murder coincide with the publication of Public Health England’s ‘Disparities in the risk and outcomes of COVID-19’ report, which states that “Death rates from COVID-19 were highest among people of Black and Asian ethnic groups”. The report concedes that this is the result of racial inequalities in the UK. In light of this, I ask that you take action on the UK’s complicity regarding the situation in the US and on other examples of structural racism closer to home, including those related to COVID-19.

    1. Regarding UK exportation of tear gas and rubber bullets to the US:

I support Black Lives Matter UK (BLMUK) and the Labour party’s condemnation of the violent response by the US government and police forces towards protestors. I also ask that you recognise the UK’s complicity in this violence through the sale of munitions to the US, and that you pressure the UK government to cease its export of rubber bullets, tear gas, riot shields and all other weapons that are being used against civilians in the US. 

    2. Regarding police violence in the UK:

Police brutality and a lack of accountability is not unique to the US. Between 1990 and 2019 there were 1,741 deaths in police custody or following contact with the police in England and Wales, yet the last time a British police officer was convicted for a death in custody was in 1969. Private security firms contracted by the government are no less at fault. In 2010, Jimmy Mubenga was killed on a deportation flight by a G4S security guard; like George Floyd and Eric Garner, his final words were “I can’t breathe.” I ask that you pressure the UK government to hold the police and privately contracted security firms fully accountable for their actions, and that the government devise an action plan that will ensure an end to police brutality and institutional racism. 

    3. Regarding the Public Health England (PHE) report “Disparities in the risk and outcomes of COVID-19” and structural racism in the UK:

The PHE report indicates that people from BAME backgrounds have been disproportionately affected by COVID-19 in the UK in part as a result of being more likely to live in urban/deprived areas and overcrowded households and to be in jobs that present a higher risk of exposure. Echoing another BLMUK demand, I ask that you pressure the UK government to provide a detailed response plan to the findings in this report, and in particular to the ways in which it lays bare the structural racism, reinforced by government policy, that is implicated in these deaths.

    4. Regarding the Hostile Environment, migrant rights and access to healthcare:

Though the PHE report mentions “cultural and language differences” as a barrier to accessing health services, it fails to address the manner in which Hostile Environment healthcare charging policies have demonstrably deterred migrants, many of whom are BAME, from accessing the NHS. Though treatment for infectious diseases like COVID-19 is exempt from charging, mistrust of healthcare settings, concerns around data sharing and fear about charges relating to other conditions can deter migrants from seeking treatment. Just last month, The Independent reported the case of Elvis, a Filipino man in the UK who died from the coronavirus after being too afraid to seek care.

I echo Patients Not Passports in calling for an end to NHS charging for migrants and a moratorium on all data sharing with the Home Office. The government must launch an information campaign to alert migrant communities of their rights to ensure that nobody is deterred from seeking care. In addition, a firewall should be established to ensure that all data gathered in the process of providing urgent services, ranging from healthcare to housing, cannot be used for the purposes of immigration control.

    5. Regarding workplace safety practices and accountability under COVID-19:

Following the death of Belly Mujinga, I join her husband Lusamba Katalay in asking that you and your party demand an investigation into Govia Thameslink Railway (GTR) regarding workplace safety and provision of PPE. GTR knew that Ms. Mujinga had underlying health problems. Yet they continued to place her on the front lines of the virus, without appropriate PPE and seemingly without concern for her safety or the safety of her co-workers.

I therefore also ask that the government require employers of essential workers to provide PPE and appropriately safeguard those at risk or with household members at higher risk of complications from the virus, such as by supporting paid leave or alternative work arrangements. I join the Transport Salaried Staffs’ Association (TSSA) in requesting an expansion of the Coronavirus Compensation Scheme to include not only care workers but also transport workers, and also ask that this be extended to all key workers.

    6. Regarding the systemic oppression of BAME communities through Government policy:

Though these coronavirus deaths are not as obvious as a case in which a police officer is filmed in the act of murder, the state is still responsible for deaths caused by systemic exclusion, disenfranchisement, underfunding and neglect fueled by racism and unconscious bias. As this month marks the 3-year anniversary of the Grenfell Tower fire, another example of indirect state violence against BAME and poor/working class people in the UK, I demand those responsible for the fire be held accountable and demand an end to policies like stop and search, Prevent and No Recourse to Public Funds (NRPF) that disproportionately neglect, underfund, and criminalise BAME communities.

Please let me know the actions that you and your party plan to put in place in response to these demands.

Yours sincerely,

{u[name]}
{u[address]}
    """,
)


def get_existing_templates():
    """Grab all the template options that exist so far"""
    """
    IMPORTANT: Gavin Williamson template removed until we can find a way to contanct him via his preferred method for enquiries about educations
    """
    return deepcopy(
        # [mp_police, gavinwilliamson_email, belly_mujinga_mp, belly_mujinga_govia]
        [mp_police, belly_mujinga_mp, belly_mujinga_govia, shukri_abdi, mp_solidarity, mp_lgsmigrants]
    )
