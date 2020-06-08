from emailtemplates import add_new_template


# Want this to fail if reference exists already
add_new_template(
    reference="mp_police_equipment",
    subject="Suspension of Exportation of Policing Equipment to the US",
    body="""
Dear {t[name]},


My name is {u[name]} and I am a resident of {t[constituency]}, at {t[address]}.

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


add_new_template(
    reference="belly_mujinga_mp",
    subject="Justice for Belly Mujinga",
    body="""
Dear {t[name]},

My name is {u[name]} and I am a resident of {t[constituency]}, at {t[address]}.

I write further to my previous email regarding Black Lives Matter with a specific demand for justice for Belly Mujinga, a railway ticket office worker who contracted COVID-19 and subsequently died. I am sure you are aware that Mujinga, a key worker, was spat on by a member of the public claiming he was infectious on March 21.

Despite this event taking place, a spokesperson for British Transport Police has recently stated that they will take no further action into the case, given that the “tragic death of Belly Mujinga was not a consequence of this incident.”

However, in Glasgow, a man who spat at a police officer and joked about coronavirus has been jailed for twelve months.

I recognise that there may be legal differences between each of the four nations, but it is unconscionable to me that there is such a gulf between the consequences of these two actions. Regardless of whether illness may or may not be attributed to the assault, it is an assault nonetheless, and an assault that in the case of Belly Mujinga has not been given due weight.

I find this especially troubling following the report published into disproportionate BAME deaths due to COVID-19, and ask whether Belly Mujinga - a Congolese woman with underlying health issues, who was reportedly scared for her life - was a victim of a poor response to the coronavirus pandemic on the part of British authorities.

I urge the UK government to seek to reopen the investigation into the assault on Belly Mujinga.

Yours sincerely,

{u[name]}""",
)
