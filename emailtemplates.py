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

    def set_target(self, name, email, ward=None):
        self.target = {"name": name, "email": email, "ward": ward}

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
    "ward": "Westminster",
    "email": "bigbadboi@hotmail.co.uk",
}

mp_police = EmailTemplate(
    subject="Suspension of Exportation of Policing Equipment to the US",
    body="""
Dear {t[name]},


My name is {u[name]} and I am a resident of {t[ward]}.
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

{u[name]}""",
)
gavinwilliamson_email.set_target(
    name="Secretary of State for Education", email="gavin.williamson.mp@parliament.uk"
)

belly_mujinga_mp = EmailTemplate(
    subject="Justice for Belly Mujinga",
    body="""
Dear {t[name]},

My name is {u[name]} and I am a resident of {t[ward]} ward.

I write further to my previous email regarding Black Lives Matter with a specific demand for justice for Belly Mujinga, a railway ticket office worker who contracted COVID-19 and subsequently died. I am sure you are aware that Mujinga, a key worker, was spat on by a member of the public claiming he was infectious on March 21.

Despite this event taking place, a spokesperson for British Transport Police has recently stated that they will take no further action into the case, given that the “tragic death of Belly Mujinga was not a consequence of this incident.”

However, in Glasgow, a man who spat at a police officer and joked about coronavirus has been jailed for twelve months.

I recognise that there may be legal differences between each of the four nations, but it is unconscionable to me that there is such a gulf between the consequences of these two actions. Regardless of whether illness may or may not be attributed to the assault, it is an assault nonetheless, and an assault that in the case of Belly Mujinga has not been given due weight.

I find this especially troubling following the report published into disproportionate BAME deaths due to COVID-19, and ask whether Belly Mujinga - a Congolese woman with underlying health issues, who was reportedly scared for her life - was a victim of a poor response to the coronavirus pandemic on the part of British authorities.

I urge the UK government to seek to reopen the investigation into the assault on Belly Mujinga.

Yours sincerely,

{u[name]}""",
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

Until responsible actions are taken to honour the death of Belly and prevent the future assault of your workers and you take full responsibility for your role in Belly's murder, I have decided to boycott southern rail, Gatwick express, Great northern and Thameslink.

Regards,

{u[name]}""",
)
belly_mujinga_govia.set_target(
    name="Patrick Verwer", email="Patrick.Verwer@gtrailway.com"
)


def get_existing_templates():
    """Grab all the template options that exist so far"""
    return deepcopy(
        [mp_police, gavinwilliamson_email, belly_mujinga_mp, belly_mujinga_govia]
    )
