import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import useApi from '../hooks/APIHandler';
import {
  Box,
  Card,
  CardContent,
  Tabs,
  Tab,
  TextField,
  Button,
  Typography,
  LinearProgress,
} from '@mui/material';
import { toast } from 'react-toastify';

// Hàm xử lý form đăng nhập
const LoginForm = ({ username, password, setUsername, setPassword }) => {
  const navigate = useNavigate();
  const { callApi, error, loading } = useApi();

  const doLogin = async (e) => {
    e.preventDefault();
    let response = await callApi({
      url: "http://127.0.0.1:8000/api/auth/login/",
      method: "POST",
      body: { username, password }
    });
    if(response?.data?.access){
      localStorage.setItem("token", response.data.access);
      toast.success("Login Successfully !");
      navigate("/home");

    }
    else{
      toast.error("Invalid Credentials!");
    }
    console.log(response);
  };

  return (
    <form onSubmit={doLogin}>
      <TextField
        label="Username"
        name="username"
        variant="outlined"
        fullWidth
        margin="normal"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <TextField
        label="Password"
        type="password"
        name="password"
        variant="outlined"
        fullWidth
        margin="normal"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      {loading?<LinearProgress style={{width: '100%'}}/>:
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ marginTop: 2 }}>
        Login
      </Button>}
    </form>
  );
};

// Hàm xử lý form đăng ký
const SignupForm = ({ username, email, password, setUsername, setEmail, setPassword }) => {
  const navigate = useNavigate();
  const { callApi, error, loading } = useApi();

  const doSignup = async (e) => {
    e.preventDefault();
    let response = await callApi({
      url: "http://127.0.0.1:8000/api/auth/signup/",
      
      method: "POST",
      body: { username, email, password, profile_pic: "link" }
    });
    if(response?.data?.access){
      localStorage.setItem("token", response.data.access);
      toast.success("Signup Successfully !");
      navigate("/home");

    }
    else{
      toast.error("Signup failed !");
    }
    console.log(response);
  };

  return (
    <form onSubmit={doSignup}>
      <TextField
        label="Username"
        variant="outlined"
        fullWidth
        margin="normal"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <TextField
        label="Email"
        type="email"
        variant="outlined"
        fullWidth
        margin="normal"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <TextField
        label="Password"
        type="password"
        variant="outlined"
        fullWidth
        margin="normal"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      {loading?<LinearProgress style={{width: '100%'}}/>:
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ marginTop: 2 }}>
        Sign Up
      </Button>}
    </form>
  );
};

const AuthScreen = () => {
  const [value, setValue] = useState(0);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleTabChange = (event, newValue) => {
    setValue(newValue);
  };

  useEffect(()=>{
    if(localStorage.getItem("token")){
      navigate("/home");
    }
  },[])

  return (
    <Box display="flex" justifyContent="center" alignItems="center" height="100vh" bgcolor="#f5f5f5">
      <Card sx={{ width: 400 }}>
        <CardContent>
          <Typography variant="h5" component="div" align="center">
            {value === 0 ? 'Login' : 'Sign Up'}
          </Typography>
          <Tabs value={value} onChange={handleTabChange} centered>
            <Tab label="Login" />
            <Tab label="Sign Up" />
          </Tabs>
          {value === 0 ? (
            <LoginForm
              username={username}
              password={password}
              setUsername={setUsername}
              setPassword={setPassword}
            />
          ) : (
            <SignupForm
              username={username}
              email={email}
              password={password}
              setUsername={setUsername}
              setEmail={setEmail}
              setPassword={setPassword}
            />
          )}
        </CardContent>
      </Card>
    </Box>
  );
};

export default AuthScreen;
