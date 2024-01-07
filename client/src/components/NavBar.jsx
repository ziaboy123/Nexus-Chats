import { useContext } from "react";
import { Container, Nav, Navbar, Stack } from "react-bootstrap";
import {Link} from "react-router-dom"
import { AuthContext } from "../context/AuthContext";


const NavBar = () => {

    const { user, logoutUser } = useContext(AuthContext);

    return <Navbar bg="dark" className="mb-4" style={{ height:"3.75rem"}}>
        <Container>
            <h2>
                <a href="http://127.0.0.1:5465/" className="text-decoration-none" style={{color: 'cyan'}}>
                    The Link Network
                </a>
            </h2>
            {user && (
                <span className="text-danger">Welcome {user?.name} to Nexus!</span>
            )}
            <Nav>
                <Stack direction="horizontal" gap={3}>
                    {user && (
                        <>
                            <Link 
                                onClick={() => logoutUser()} 
                                to="/login" 
                                className="link-light text-decoration-none"
                            >
                                Logout
                            </Link>
                        </>
                    )}

                    {!user && (
                        <>
                            <Link to="/login" className="link-light text-decoration-none">
                                Login
                            </Link>
                            <Link to="/register" className="link-light text-decoration-none">
                                Register
                            </Link>
                        </>
                    )}
                    
                </Stack>
            </Nav>
        </Container>
        </Navbar>;
};
 
export default NavBar;
