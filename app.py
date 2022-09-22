import justpy as jp
from src.voiceactor import VA
app = jp.app

session_data = {}

def animate(self, msg):
    msg.page.divalert.components.remove(msg.page.divalert.components[0])

@jp.SetRoute('/va')
def va_display(request):
    
    try:
        if session_data[request.session_id]:
            username = ""

    except KeyError:
        return jp.redirect('/')

    username = session_data[request.session_id][0]['value']
        
    v = VA(username=username)

    dict = v.info_url()

    if len(dict) > 100:
        range = 100

    else:
        range = len(dict)
        
    wp = jp.WebPage(title="VA Count", favicon='/assets/favicon.ico')
    root = jp.Div(a=wp)

    wp.head_html = """<script src="https://cdn.tailwindcss.com"></script>"""
    
    section = jp.Section(classes='h-full bg-cover bg-gray-900 font-sans', a=root)
    crow = jp.Div(classes='grid grid-flow-row auto-rows-max', a=section)
    charlen = ""

    for va, char in dict[:range]:
        
        div1 = jp.Div(classes='grid grid-flow-row auto-rows-max', a=crow)
        
        column1 = jp.Div(a=div1)
        section1 = jp.Section(classes='overflow-hidden bg-gray-900', a=column1)
        container1 = jp.Div(classes='rounded-lg container bg-gray-900 px-4 py-2 mx-auto lg:pt-12 lg:px-32', a=section1)
        div2 = jp.Div(classes='flex flex-wrap -m-4 md:-m-4', a=container1)
        card = jp.A(href=va[1], classes='''flex flex-col rounded-lg 
            border shadow-md md:flex-row md:max-w-md border-gray-800 bg-gray-800 hover:bg-gray-700''', a=container1)
        vaimg = jp.Img(classes='object-cover w-full h-96 justify-start rounded-t-lg md:h-auto md:w-48 md:rounded-none md:rounded-l-lg', src=va[2], alt='', a=card)
        div2 = jp.Div(classes='flex flex-col justify-center p-4 leading-normal', a=card)
        vaname = jp.H5(classes='mb-2 text-2xl font-bold text-white tracking-tighttext-white', a=div2, text=va[0])


        if len(char) == 1:
            charlen = " character"
        else:
            charlen = " characters"

        charcnt = jp.P(classes='mb-3 text-base font-normal text-gray-400', a=vaname, text='voiced ' + str(len(char)) + charlen)

                
        column2 = jp.Div(a=div1)
        section1 = jp.Section(classes='overflow-hidden text-gray-900 ', a=column2)
        container1 = jp.Div(classes='container px-4 py-2 mx-auto lg:pt-12 lg:px-32', a=section1)
        div2 = jp.Div(classes='flex flex-wrap -m-1 md:-m-2', a=container1)
        spacer = jp.Div(classes='p-4 space-y-3', a=container1)

        for c in char:
            div3 = jp.Div(classes='w-1/6', a=div2)
            div4 = jp.Div(classes='w-full p-100 md:p-3', a=div3)
            div5 = jp.A(href=c[1], a=div4)
            div6 = jp.Div(classes='overflow-hidden rounded-xl relative group', a=div5)
            div7 = jp.Div(classes='''z-50 opacity-0 group-hover:opacity-100 transition duration-300 ease-in-out cursor-pointer absolute from-black/80 
                to-transparent bg-gradient-to-t inset-x-0 -bottom-2 pt-30 text-white flex items-end''', a=div6)
            div8 = jp.Div(a=div7)
            div9 = jp.Div(classes='p-4 space-y-3 text-xl', a=div8)
            charname = jp.Div(classes='font-bold', a=div9, text=c[0])
            div10 = jp.Div(classes='opacity-60 text-sm ', a=div9)
            charimg = jp.Img(alt='', classes='object-cover w-full group-hover:scale-110 transition duration-300 ease-in-out', 
                src=c[2], a=div6)
        
    return wp

@jp.SetRoute('/')
def commands_demo():

    wp = jp.WebPage(title="VA Count", favicon='/assets/favicon.ico')

    wp.head_html = """<script src="https://cdn.tailwindcss.com"></script>"""

    root = jp.Div(a=wp)
    section = jp.Section(classes='h-screen bg-cover bg-gray-900 font-sans', a=root)
    container = jp.Div(classes='flex h-screen items-center justify-center container mx-auto px-8', a=section)
    div1 = jp.Div(classes='max-w-5xl text-center', a=container)
    title = jp.H1(classes='text-4xl sm:text-4xl capitalize tracking-widest text-white lg:text-7xl', a=div1, text='Unofficial AniList VA Count')
    div2 = jp.Div(classes='max-w-4xl text-center', a=container)
    aux = jp.Div(classes='flex h-24 items-center justify-center container mx-auto px-8', a=div2)
    description = jp.P(classes='mt-5 lg:text-lg text-white', a=div2, text='''This is a small website that uses AniList\'s API to get 
        the total number of characters voiced by a voice actor, based on a user\'s completed anime list. In AniList\'s stats page for Staff, 
        only main characters are  counted towards statistics, which leads to some differences if every character were to be counted. ''')
    instruction = jp.P(classes='mt-6 lg:text-lg text-white', a=div2, text='Enter your AniList\'s username below to see your top voice actors.')
    div3 = jp.Div(classes='mt-8 flex flex-col space-y-3 sm:-mx-2 sm:flex-row sm:justify-center sm:space-y-0', a=div2)
    form1 = jp.Form(a=div3)
    in1 = jp.Input(input=animate, placeholder='username', a=form1, classes='form-input', required=True)
    submit_button = jp.Input(onclick=animate, value='Search', type='submit', a=form1, classes='''bg-blue-500 hover:bg-blue-400 text-white 
        font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded m-2''')
    wp.divalert = jp.Div(classes='flex h-24 items-center justify-center container mx-auto px-8', a=form1)

    def submit_form(self, msg):

        session_data[msg.session_id] = msg.form_data

        for data in session_data.values():
            username = data[0]['value']
        
        v = VA(username=username)

        user = v.get_user()
        
        if user['data']['User']:
            
            if not user['data']['MediaListCollection']['lists']:
                root = wp.divalert
                alert = jp.Div(click=animate, animation=f'''fadeIn{'Up'}''', 
                    classes='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative', role='alert', a=wp.divalert)
                alertinfo = jp.Span(classes='block sm:inline', a=alert, text='This user does not have a completed anime list')
            
            else:
                msg.page.redirect = '/va'

        else:
            root = wp.divalert
            alert = jp.Div(click=animate, animation=f'''fadeIn{'Up'}''', 
                classes='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative', role='alert', a=wp.divalert)
            alertinfo = jp.Span(classes='block sm:inline', a=alert, text='User was not found')
            
    form1.on('submit', submit_form)

    return wp

jp.justpy(commands_demo)