import './App.css';
import Layout from './layout/layout';
import Auth from './pages/Auth';
import Home from './pages/Home';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import 'react-toastify/dist/ReactToastify.css';
import ProtectedRoute from './utils/ProtectedRoute';
import { ToastContainer } from 'react-toastify';

const sidebarItems = [
  { name: "Home", link: "/home", icon: "home" },
  { name: "Products", link: "/products", icon: "products" },
  { name: "Categories", icon: "categories", children: [
      { name: "All Categories", link: "/categories" },
      { name: "Add Categories", link: "/categories/add" }
    ]
  },
  { name: "Orders", link: "/orders", icon: "orders" },
  { name: "Users", link: "/users", icon: "users" },
  { name: "Settings", link: "/settings", icon: "settings" },
];

const router = createBrowserRouter([
  { path: "/auth", element: <Auth /> },
  {
    path: "/",
    element: <Layout sidebarList={sidebarItems} />,
    children: [
      {
        path: "home", 
        element: <ProtectedRoute><Home /></ProtectedRoute>
      }
    ]
  },
]);

function App() {
  return (
    <>
      <RouterProvider router={router} />
      <ToastContainer position="bottom-right" autoClose={3000} hideProgressBar={false} style={{ marginBottom: '30px' }} />
    </>
  );
}

export default App;
