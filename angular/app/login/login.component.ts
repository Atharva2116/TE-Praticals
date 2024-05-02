
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  constructor(private router: Router) { }

  login(): void {
    const emailInput = (<HTMLInputElement>document.getElementById('username')).value;
    const passwordInput = (<HTMLInputElement>document.getElementById('password')).value;

    if (emailInput.trim() === "" || passwordInput.trim() === "") {
      alert("Fill in the details");
    } else {
      localStorage.setItem('Email', emailInput);
      localStorage.setItem('Password', passwordInput);
      this.router.navigate(['/profile']);
      alert("Successfully Logged in");
    }
  }
}
