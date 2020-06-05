# -*- coding: utf-8 -*-

# import win32com.client as win32
import urllib.request, json
import requests
from bs4 import BeautifulSoup


class EmailTemplate:
    def __init__(self, targetname, targetemail, subject, body, cc=None):
        self.name = targetname
        self.email = targetemail
        self.subject = subject
        self.body = "Dear {},<br><br>\n\n".format(self.name) + body
        self.cc = cc

    def __str__(self):
        return str([self.name,self.email,self.subject,self.body,self.cc])


def MPpoliceEmail(name, toname, ward, mpEmail):

    subjectstring = "Suspension of Exportation of Policing Equipment to the US"

    emailstring = """My name is {} and I am a resident of {}.
        <br><br>
        I am writing to you today to implore you to put pressure on the government to stop the exportation of tear gas, rubber bullets and riot shields to the United States and to condemn Trump's use of force against his own citizens.
        <br><br>
        After the shocking footage of the police and the national guard using excessive force against Black Lives Matter protesters across the United States, the UK should immediately stop all policing and security equipment export to the US where there is a clear risk of further misuse. This is something the UK is obligated to do under its own laws.
        <br><br>
        Given the evidence emerging from multiple US cities, there is a very real risk of UK-manufactured tear gas or rubber bullets being used against George Floyd protesters in dangerous and highly inappropriate ways - ministers must respond to this.
        <br><br>
        Ministers should be making detailed case by case assessments of any requests for equipment from individual US police forces – withholding exports from any that have clearly acted irresponsible during the current crisis. The UK has an obscene track record of looking the other way when UK arms and security equipment is misused overseas. Now is the time to change that.
        <br><br>
        In addition to immediate suspension of UK sales of tear gas, riot shields and rubber bullets to the US, the UK Government should condemn Trump's use of force against his own citizens. The behaviour he has exhibited is anti-democratic and cruel. It sets a dangerous precedent and the UK government must acknowledge this.
        <br><br>
        In short, my requests to you are:<br>
        -   	Immediate stopping of UK sales of teargas, riot shield and rubber bullets to the US<br>
        -   	Condemnation of Trump's use of force against his own citizens
        <br><br>
        Thank you for your time. Please respond to this email as soon as you see fit.
        <br><br>
        Regards,
        <br><br>
        {}
        """.format(
        name, ward, name
    )

    return EmailTemplate(toname, mpEmail, subjectstring, emailstring)


def gavinwilliamsonEmail(name, mpEmail):

    subjectstring = "Make Black histories mandatory in the national curriculum"

    emailstring = """As supporters of The Black Curriculum, we are dismayed by the events of the last few weeks which have disproportionately affected Black people in the UK - exacerbated by Covid19, and the subsequent lack of response by those in authority. Thousands of us, the British voting public are grief stricken and concerned about the existing status-quo in the UK, which disregards the lives and contributions of Black British people. We would like to bring to your attention some of the structural inequalities in the UK, especially pertaining to education and the national curriculum.
        <br><br>
        As you are aware, the national curriculum excludes Black histories throughout, and omits the vast contributions Black people have made to the UK. As a result, young people who learn from the national curriculum are not given a full or accurate version of British history, which limits their opportunities and futures in an increasingly diverse landscape. Despite numerous calls over the years to reform the national curriculum to incorporate Black histories, these requests have been denied. Learning Black history should not be a choice but should be mandatory. Our curriculum should not be reinforcing the message that a sizeable part of the British population are not valued.
        <br><br>
        Black people have been in Britain since Roman times, have contributed to and shaped the foundation of our society. Therefore, we are asking you to specifically include Black histories on the national curriculum from KS1 - KS4 to include Black British histories across different subject areas, including History, Citizenship, English and PSHE. By doing so, you can invest in the lives and opportunities of all young people across the UK to become fully rounded citizens and create a better, fairer society. This is in line with the DfE Strategy’s first principle as highlighted in 2015-2020 World-class Education and Care:
        <br><br>

                                “Our first principle is to ensure each policy puts children and
                                young people first. We must not let anything detract from
                                improving the lives and opportunities of those who rely on the
                                education and children social care systems.” – p.11, DfE strategy 2015-2020
        <br><br>
        The Black Curriculum is demanding that you work with them to adequately incorporate Black British history into the national curriculum and to fulfil your goals of British education truly being able to help the government’s “commitments to social justice and economic growth.”
        <br><br>
        Will you meet with the leaders of the Black Curriculum? They are ready and waiting for your response.
        <br><br>

        With thanks,
        <br><br>

        {}
        """.format(
        name
    )
    return EmailTemplate(
        "Secretary of State for Education",
        "gavin.williamson.mp@parliament.uk",
        subjectstring,
        emailstring,
        cc=mpEmail,
    )


def MPbellymujingaEmail(name, toname, ward, mpEmail):

    subjectstring = "Justice for Belly Mujinga"

    emailstring = """My name is {} and I am a resident of {} ward.
        <br><br>

    I write further to my previous email regarding Black Lives Matter with a specific demand for justice for Belly Mujinga, a railway ticket office worker who contracted COVID-19 and subsequently died. I am sure you are aware that Mujinga, a key worker, was spat on by a member of the public claiming he was infectious on March 21.
        <br><br>

    Despite this event taking place, a spokesperson for British Transport Police has recently stated that they will take no further action into the case, given that the “tragic death of Belly Mujinga was not a consequence of this incident.”
        <br><br>

    However, in Glasgow, a man who spat at a police officer and joked about coronavirus has been jailed for twelve months.
        <br><br>

    I recognise that there may be legal differences between each of the four nations, but it is unconscionable to me that there is such a gulf between the consequences of these two actions. Regardless of whether illness may or may not be attributed to the assault, it is an assault nonetheless, and an assault that in the case of Belly Mujinga has not been given due weight.
        <br><br>

    I find this especially troubling following the report published into disproportionate BAME deaths due to COVID-19, and ask whether Belly Mujinga - a Congolese woman with underlying health issues, who was reportedly scared for her life - was a victim of a poor response to the coronavirus pandemic on the part of British authorities.
        <br><br>

    I urge the UK government to seek to reopen the investigation into the assault on Belly Mujinga.
        <br><br>

    Yours sincerely,
        <br><br>

    {}
    """.format(
        toname, name, ward, name
    )
    return EmailTemplate(toname, mpEmail, subjectstring, emailstring)


def goviaBellymujingaEmail(name):

    subjectstring = "Justice for Belly Mujinga"

    emailstring = """I am writing to you in regards to the recent death of Belly Mujinga, who worked for Govia Thameslink Railway. Her death follows after an assault was carried out on 21st March in which her and colleagues were spat at and coughed on during their shift at London Victoria Station.
        <br><br>

    As I am sure you are aware, it was revealed on 29th May that The British Transport Police ruled that they believed there was no link between the act of assault and her death and stated that ‘no further action will be taken’, closing the case. In spite of this Ms. Mujinga’s passing on 5th April comes just two weeks after the assault had taken place and after several days having been admitted to hospital and testing positive for COVID-19.
        <br><br>

    Following the outcome in regards to Ms. Mujinga’s death and The British Transport Police’s dismissal of the case, I urge you as CEO of Govia Thameslink Railway, to take action on her behalf and to that of her loved ones following her death. As an essential worker, Ms. Mujinga was failed by the Govia Thameslink Rail to be protected after she had expressed concerns for her wellbeing due to respiratory issues. Ms. Mujinga made appeals to work away from crowds at the busy station due to there being no PPE provided for railway workers, her concerns were inadequately dismissed.
        <br><br>

    In spite of the assault carried out and Ms. Mujinga’s passing it was reported by The Independent in an article released on 14th May by a worker at London Victoria station that “There’s not much being done to check all the staff, today is the first day we have had masks.” Going forward, it shows that you have not prioritised the protection and the safety of your staff to prevent such an act happening again in the future.
        <br><br>

    So I ask, why did you ignore Belly’s requests to work away from crowds during the pandemic as she had underlaying health issues?
        <br><br>

    Further, why did it take weeks for Govia to surrender the CCTV footage to the police?
        <br><br>

    As a concerned individual I urge you to recognise the needs of more effective regulations and protection of railway workers at Govia Thameslink Rail during this time and for an assault similar to that of Ms Mujinga which effectively cost her life does not take place again.
        <br><br>

    Until responsible actions are taken to honour the death of Belly and prevent the future assault of your workers and you take full responsibility for your role in Belly's murder, I have decided to boycott southern rail, Gatwick express, Great northern and Thameslink.
        <br><br>

    Regards
        <br><br>

    {}
    """.format(
        name
    )
    return EmailTemplate(
        "Patrick Verwer", "Patrick.Verwer@gtrailway.com", subjectstring, emailstring
    )


def getGovDetails(postcode):

    url_base = "http://api.postcodes.io/postcodes/"
    with urllib.request.urlopen(url_base + postcode) as url:
        data = json.loads(url.read().decode())
        if data["status"] == 200:
            topdata = data["result"]
        else:
            raise KeyError("No postcode found!")

    MPurl = (
        "http://lda.data.parliament.uk/commonsmembers.json?_view=members&_pageSize=2097&_page=0&constituency.label="
        + "%20".join(topdata["parliamentary_constituency"].split(" "))
    )

    with urllib.request.urlopen(MPurl) as url:
        MPdata = json.loads(url.read().decode())

        for possibleMP in MPdata["result"]["items"]:
            MPid = (possibleMP["_about"]).split("/")[-1]
            print("Checking MP: {}".format(possibleMP["fullName"]))

            try:
                MPurl = "https://members.parliament.uk/member/{}/contact".format(MPid)
                MPemails = emailExtractor(MPurl)  # MP email (in a list)
                assert len(MPemails) > 0
                myward = topdata["admin_ward"]  # User's ward
                MPname = possibleMP["fullName"]["_value"]
                print(
                    "Found correct MP: {}. {} emails found".format(
                        MPname, len(MPemails)
                    )
                )
                break
            except:
                pass

    return {"ward": myward, "MPemail": MPemails, "MPname": MPname}


def emailExtractor(urlString):
    emailList = []
    getH = requests.get(urlString)
    h = getH.content
    soup = BeautifulSoup(h, "html.parser")
    mailtos = soup.select("a[href^=mailto]")
    for i in mailtos:
        href = i["href"]
        try:
            str1, str2 = href.split(":")
        except ValueError:
            break

        emailList.append(str2)
    return emailList


# def Emailer(et):
#     ### Change to dict on this and on all email writing functions
#     try:
#         recipient = et.email
#         subject = et.subject
#         copiedin = et.cc
#         text = et.subject

#         outlook = win32.Dispatch("Outlook.Application")
#         mail = outlook.CreateItem(0)
#         mail.To = recipient
#         mail.Subject = subject
#         mail.HtmlBody = text
#         if copiedin:
#             mail.CC = copiedin
#         mail.Save()
#         print("Email done")
#     except:
#         print("One email failed")


def draftEmails(myname, postcode):
    ret = getGovDetails(postcode)
    ward = ret["ward"]
    MPname = ret["MPname"]
    MPemails = ret["MPemail"]

    print(
        "Details found. You live in {} ward and your MP is {}, with email(s): {}".format(
            ward, MPname, MPemails
        )
    )

    filled_email_templates = []

    for MPemail in MPemails:
        filled_email_templates.append(
            MPpoliceEmail(myname, MPname, ward, MPemail)
        )
        filled_email_templates.append(
            MPbellymujingaEmail(myname, MPname, ward, MPemail)
        )

    filled_email_templates.append(gavinwilliamsonEmail(myname, MPemails[0]))
    filled_email_templates.append(goviaBellymujingaEmail(myname))

    for email in filled_email_templates:
        print(email)
        # Emailer(email)


myname = input("Please enter your full name (case sensitive): ")
mypost = input(
    "Please enter your postcode (this will only be used to find your MP's email address): "
)

draftEmails(myname, mypost)

print(
    "There should now be emails drafted in your Outlook app. Please check over them and send them at your own discretion"
)
print(
    "If you had any issues with this application, would like to add email templates to it, or want to help improve it, please contact Puria at pr450@cam.ac.uk"
)
_ = input("BLACK LIVES MATTER")
