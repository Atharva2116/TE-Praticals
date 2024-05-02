import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  username: string;
  password: string;
  constructor() {
    this.username = '';
    this.password = '';
  }
  ngOnInit(): void {
    this.username = localStorage.getItem('Email') || '';
    this.password = localStorage.getItem('Password') || '';
  }
}
