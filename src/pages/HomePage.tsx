import landingImage from "../assets/hero.png"

const HomePage = () => {
    return(
       <div className="flex flex-col gap-12">
            <div className="md:px=32 bg-white rounded-lg shadow-md py-8 flex flex-col gap-5 text-center -mt-16">
                <h1 className="text-3x1 font-bold tracking-tight justify-centre text-green-600">
                    Empowering You to make a difference, one meal at a time!
                </h1>
                <span className="text-x1">Cook smarter, waste less!</span>
            </div>
            <div className="grid md:grid-cols-2 gap-5">
                <img src={landingImage} />
                <div className="flex flex-col items-centre justify-centre gap-4 text-centre">
                    <span className="font-bold text-3x1 tracking-tighter">
                        Get to donate and help faster than ever before!
                    </span>
                    <span>
                        Checkout EmpowerWave to ensure responsible consumption and production!
                    </span>
                </div>
            </div>
       </div> 
    );
};

export default HomePage;