
import './App.css';
import Layout from './utils/Layout';
import AuthScreen from './pages/AuthScreen';
import Home from './pages/Home';
import { createBrowserRouter, RouterProvider } from 'react-router-dom'; // ✅ Đúng
import 'react-toastify/dist/ReactToastify.css';


const router = createBrowserRouter([
  { path: "/", element: <AuthScreen /> },
  { path: "/home", element: <Home /> }
]);

function App() {
  return (
    
    <Layout>
      <RouterProvider router={router}/>

    </Layout>
    
  )
}

export default App;
