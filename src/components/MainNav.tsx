import { Button } from "./ui/button";

const MainNav = () => {
    return(
        <Button
          variant="ghost"
          className="font-bold hover:text-green-500 hover:bg-white"
        >
            Log In
        </Button>
    );
};

export default MainNav;