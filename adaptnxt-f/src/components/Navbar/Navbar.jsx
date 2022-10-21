import React from "react";
import styles from "../Navbar/Navbar.module.css";

function Navbar() {
  
  // const {cartdatacount} = useSelector(state=>state)
  // const navigate = useNavigate()

  return (
    <div className={styles.navbar}>
      <div style={{display:"flex",width:"35%",justifyContent:"space-between"}}>
      <h3>Walmart</h3>
      <h3>Departments</h3>
      <h3>Services</h3>
      </div>
      <div style={{marginTop:"1.5%",width:"30%",height:"30px",marginLeft:"-120px"}}>
      <input style={{width:"90%",height:"30px",border:"none",borderRadius:"10px"}} type="serach" />
      </div>
      <div style={{display:"flex",width:"20%",justifyContent:"space-around"}}>
      <h3>Login</h3>
      <h3>Cart</h3>
    </div>
    </div>
  );
}

export default Navbar;
