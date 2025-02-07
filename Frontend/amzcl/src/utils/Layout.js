import {ToastContainer} from 'react-toastify';

const Layout = ({ children }) => {
    return (
        <>
            {children}
            <ToastContainer position= "bottom-right" autoclose={3000} hideProcessBar = {false} style={{marginBottom:'30px'}} />
        </>
    );
};

export default Layout;
