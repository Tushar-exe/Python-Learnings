from django.http import HttpResponse


def index(request):
    index_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 100%;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
            }
            .video-background {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                z-index: -1;
            }
            .video-background video {
                min-width: 100%;
                min-height: 100%;
                width: auto;
                height: auto;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }
            .content {
                position: relative;
                z-index: 1;
                text-align: center;
                color: #fff;
                background-color: rgba(0, 0, 0, 0.7);
            }
            h1 {
                font-size: 36px;
                margin-bottom: 20px;
            }
            p {
                margin-bottom: 20px;
                line-height: 1.6;
            }
            .button {
                display: inline-block;
                padding: 12px 24px;
                background-color: #007bff;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="video-background">
                <video autoplay loop muted>
                    <source src="https://v.ftcdn.net/05/43/48/26/700_F_543482611_ctzXyEWrOT0PjzIZAJa4GhjvPC8zY7Bb_ST.mp4" type="video/mp4">
                    Check your internet connection
                </video>
            </div>
            <div class="content">
                <h1>Welcome to High Performance Computing</h1>
                <p>High Performance Computing (HPC) involves the use of supercomputers and parallel processing techniques to solve complex computational problems efficiently and rapidly.</p>
                <p>Explore how HPC can accelerate your research and computations.</p>
                <a href="https://www.netapp.com/data-storage/high-performance-computing/what-is-hpc/#:~:text=High%20performance%20computing%20(HPC)%20is,3%20billion%20calculations%20per%20second." class="button">Get Started</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(index_str)



def about(request):
    about_str = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About HPC - High Performance Computing</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            .container {
                width: 100%;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
            }
            .video-background {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
            }
            .video-background video {
                min-width: 100%;
                min-height: 100%;
                width: auto;
                height: auto;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }
            .content {
                position: relative;
                z-index: 1;
                background-color: rgba(0, 0, 0, 0.7);
                padding: 40px;
                border-radius: 8px;
                text-align: center;
            }
            h1 {
                color: #fff;
                margin-top: 0;
                font-size: 36px;
                margin-bottom: 20px;
            }
            p {
                color: #fff;
                line-height: 1.8;
                margin-bottom: 20px;
            }
            @keyframes typing {
                0% {
                    width: 0;
                }
                100% {
                    width: 100%;
                }
            }
            .button {
                display: inline-block;
                padding: 12px 24px;
                background-color: #007bff;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="video-background">
                <video autoplay loop muted>
                    <source src="https://v.ftcdn.net/03/40/91/84/700_F_340918487_t9lWDbfMxM5t8jkATqaQzng5sBGiEkVy_ST.mp4" type="video/mp4">
                    connect to internet first
                </video>
            </div>
            <div class="content">
                <h1>About High Performance Computing</h1>
                <p>High Performance Computing (HPC) involves the use of supercomputers and parallel processing techniques to solve complex computational problems efficiently and rapidly.</p>
                <p>HPC plays a crucial role in various fields including scientific research, engineering simulations, weather forecasting, and financial modeling.</p>
                <p>This website aims to provide resources and information about HPC technologies, applications, and best practices.</p>
                <a href="#" class="button">Learn More</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(about_str)

